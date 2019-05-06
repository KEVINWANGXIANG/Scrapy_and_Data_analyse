import math
import numpy

def print_dict(src_dict, level, src_dict_namestr=''):
        '''
        逐行打印dict
        :param self:类实例自身
        :param src_dict:被打印的dict
        :param level:递归level，初次调用为level=0
        :param src_dict_namestr:对象变量名称字符串
        '''
        if isinstance(src_dict, dict):
            tab_str = '\t'
            for i in range(level):
                tab_str += '\t'
            if 0 == level:
                print(src_dict_namestr,'= {')
            for key, value in src_dict.items():
                if isinstance(value, dict):
                    has_dict = False
                    for k,v in value.items():
                        if isinstance(v, dict):
                            has_dict = True
                    if has_dict:
                        print(tab_str,key,":{")
                        print_dict(value, level + 1)
                    else:
                        print(tab_str,key,':',value)
                else:
                    print(tab_str,key,': ',value,)
            print(tab_str,'}')

class CTailorSamples(object):
    '''裁剪样本集'''
    def __init__(self, data_list, feat_type_list, feat_type_index, feat_value):
        self.data_list = data_list
        self.feat_type_list = feat_type_list
        self.feat_type_index_tailed = feat_type_index
        self.feat_value_tailed = feat_value

        self.tailer_work()#裁剪

    def get_samples(self):
        '''
        返回裁剪后的样本集，特征类型列表
        '''
        return self.data_list, self.feat_type_list

    def get_all_indexs(self, src_list, dst_value):
        '''
        返回给定值的所有元素的下标
        src_list = [10,20,30,30,30,50]
        e = 30
        indexs_list = tailor.get_all_indexs(src_list, e)
        print(indexs_list) #[2, 3, 4]
        '''
        dst_val_index = [i for i,x in enumerate(src_list) if x == dst_value]
        return dst_val_index

    def tailer_work(self):
        '''裁剪得到新的特征列表'''
        del self.feat_type_list[self.feat_type_index_tailed]


        '''裁剪数据集'''
        #摘取被删除的特征列
        colum_to_del = self.feat_type_index_tailed
        self.feat_value_list = [example[colum_to_del] for example in self.data_list]

        #找出含有self.feat_value_tailed特征值的所有样本所在行的下标
        rows_to_del = self.get_all_indexs(self.feat_value_list, self.feat_value_tailed)

        #删除row_index_list中行下标对应的self.src_data_list的行
        #技巧：从大的行下标开始依次删除
        #for row in list(reversed(rows_to_del)):
        #for row in rows_to_del[::-1]:
        rows_to_del.reverse()
        for row in rows_to_del:
            del self.data_list[row]

        #删除给定的特征列
        for row in range(len(self.data_list)):
            del self.data_list[row][colum_to_del]

        return self.data_list, self.feat_type_list

class CCartTree(object):
    def __init__(self, samples, feat_list, div_label, max_n_feats):
        self.samples = samples
        self.feat_list = feat_list
        self.div_label = div_label
        self.max_n_feats = max_n_feats
        self.tree_dict = {}
        self.create_tree()

    def get_tree_dict(self):
        return self.tree_dict

    def work(self, samples, feat_list, div_label, max_n_feats):
        '''
        给定样本数据集+特征列表，找出最优特征，最优切分点，最优叶节点，次优切分点
        :param samples:样本数据集
        :param feat_list:特征列表, 比如['age','work','house','credit']
        :return 样本集的最优特征，最优切分点最优叶节点
        :Note,每个样本=[ageVal, workVal, houseVal, creditVal, classLabel]
        '''
        stat, n_samples = {}, len(samples)
        class_vals = [e[-1] for e in samples]
        class_set = set(class_vals)
        for i in range(len(feat_list)):
            f, stat[f] = feat_list[i], {}#feature
            for e in samples:
                v,c = e[i], e[-1] #feature's value, feature value's class label
                if v not in stat[f].keys():
                    stat[f][v],stat[f][v]['n'],stat[f][v]['p'] = {},0,0.0
                    stat[f][v][c],stat[f][v][c]['n'],stat[f][v][c]['p'] = {},0,0.0
                elif c not in stat[f][v].keys():
                        stat[f][v][c],stat[f][v][c]['n'],stat[f][v][c]['p']={},0,0.0
                stat[f][v]['n'] += 1
                stat[f][v]['p'] = stat[f][v]['n']/n_samples
                stat[f][v][c]['n'] += 1
                #update stat[f][v][every c]['p']
                for x in class_set:
                    if x not in stat[f][v].keys():
                        stat[f][v][x],stat[f][v][x]['n'],stat[f][v][x]['p']={},0,0
                    stat[f][v][x]['p'] = stat[f][v][x]['n']/stat[f][v]['n']
                    p = float(stat[f][v][x]['p'])
                    stat[f][v][x]['gini'] = 2*p*(1-p)
                #update stat[f][v]['gini']
                d1_p, d2_p= stat[f][v]['p'], 1-stat[f][v]['p']
                prob = (class_vals.count(div_label)-stat[f][v][div_label]['n'])/(n_samples-stat[f][v]['n'])
                d1_gini, d2_gini=stat[f][v][div_label]['gini'], 2*prob*(1-prob)
                stat[f][v]['gini'] = d1_p*d1_gini + d2_p*d2_gini
        #选取最优特征，最优切分点, 最优叶子节点
        min_v_gini, bf_bv= 9527,[]
        for i in range(len(feat_list)):
            f = feat_list[i]    #visit every feature
            for v in set([e[i] for e in samples]):  #visit every value of feature
                if min_v_gini > stat[f][v]['gini']:
                    min_v_gini, bf_bv= stat[f][v]['gini'],[(f,v)]
                elif min_v_gini == stat[f][v]['gini']:
                    bf_bv.append((f,v))
        min_c_gini, bf, bv, bc= 9527,None,None,None #best
        for (f,v) in bf_bv: #存在多个相等gini的特征时，需要比较更细的条件进行筛选出一个最优特征
            for c in class_set:
                if min_c_gini > stat[f][v][c]['gini']:
                    min_c_gini = stat[f][v][c]['gini']
                    bf, bv, bc= f, v, c
                elif min_c_gini == stat[f][v][c]['gini']:
                    if stat[f][v][c]['p'] > stat[bf][bv][bc]['p']:
                        bf,bv,bc = f,v,c
        #找最优特征的次优分切点
        min_c_gini, better_v = 9527,None#better value
        bf_v_set = set([e[feat_list.index(bf)] for e in samples])
        bf_v_set.remove(bv)
        for v in bf_v_set: #存在多个相等gini的特征时，需要比较更细的条件进行筛选出一个最优特征
            if min_c_gini > stat[bf][v]['gini']:
                min_c_gini, better_v = stat[bf][v]['gini'], v
        #找最优特征的次优分切点的最优叶节点
        min_c_gini, better_c = 9527, None
        for c in class_set:
            if min_c_gini > stat[bf][better_v][c]['gini']:
                min_c_gini, better_c= stat[bf][better_v][c]['gini'], c
            elif min_c_gini == stat[bf][better_v][c]['gini']:
                if stat[bf][better_v][c]['p'] > stat[bf][better_v][better_c]['p']:
                    better_c = c
        return bf, bv, bc, better_v, better_c, stat

    def create_tree(self):
        if len(self.feat_list) < self.max_n_feats:
            return None
        #get current tree
        bf, bv, bc, better_v, better_c, stat = self.work(self.samples,
                                               self.feat_list,
                                               self.div_label,
                                               self.max_n_feats)
        root, rcond, rnode, lcond, lnode = bf, bv, bc, better_v, better_c
        print('better_c:', better_c)
        #get child tree, first to tailor samles
        tailor = CTailorSamples(self.samples,
                                self.feat_list,
                                self.feat_list.index(bf),
                                bv)
        new_samples, new_feat_list = tailor.get_samples()

        cart = CCartTree(new_samples,
                         new_feat_list,
                         self.div_label,
                         self.max_n_feats)
        child_node = cart.get_tree_dict()
        print('child_node',child_node)
        #update current tree left-child-tree
        if child_node != None and child_node != {}:
            lnode = child_node

        #current tree dict
        self.tree_dict = {}
        self.tree_dict[root] = {}
        self.tree_dict[root][rcond] = rnode
        self.tree_dict[root][lcond] = lnode
        return self.get_tree_dict()

def read_dataset(filename):
    """
    年龄段：0代表青年，1代表中年，2代表老年；
    有工作：0代表否，1代表是；
    有自己的房子：0代表否，1代表是；
    信贷情况：0代表一般，1代表好，2代表非常好；
    类别(是否给贷款)：0代表否，1代表是
    """
    fr = open(filename, 'r')
    all_lines = fr.readlines()   #list形式,每行为1个str
    labels = ['年龄段', '有工作', '有自己的房子', '信贷情况']
    dataset = []
    for line in all_lines[0:]:
        line = line.strip().split(',')   #以逗号为分割符拆分列表
        dataset.append(line)
    return dataset, labels

def read_testset(testfile):
    """
    年龄段：0代表青年，1代表中年，2代表老年；
    有工作：0代表否，1代表是；
    有自己的房子：0代表否，1代表是；
    信贷情况：0代表一般，1代表好，2代表非常好；
    类别(是否给贷款)：0代表否，1代表是
    """
    fr = open(testfile, 'r')
    all_lines = fr.readlines()
    testset = []
    for line in all_lines[0:]:
        line = line.strip().split(',')   #以逗号为分割符拆分列表
        testset.append(line)
    return testset
if __name__=='__main__':
    filename='C:/Users/Administrator/Desktop/文件/Decision_tree-python-master/dataset.txt'
    testfile='C:/Users/Administrator/Desktop/文件/Decision_tree-python-master/testset.txt'
    dataset, labels = read_dataset(filename)
    labels_tmp = labels[:] # 拷贝，createTree会改变labels
    # data_list, feat_list = create_samples()
    #由CART算法得到决策树字典
    cart = CCartTree(dataset, labels_tmp, '1', 3)
    tree_dict = cart.get_tree_dict()
    print_dict(tree_dict, 0, 'tree_dict')


