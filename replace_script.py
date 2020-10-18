#coding:utf-8
#func:关键词的全局替换
import os,shutil,time

from loguru import logger

logger.add('日志.TXT')

# CONFIG

TARGET_DIR = input('需要替换的目录:\n')

KEY_WORD = input('替换的关键词\n')

REPLACED_WORD = input("要替换为的关键词\n")

ENCODE = "utf-8"

class catalog_operation():
    def __init__(self,):
        self.files_location=[]
        self.dirs_location = []
        self.Traversal()
        print('Initialization completed')
    def Traversal(self):
        all_file_num = 0
        all_dir_num = 0

        tree = list(os.walk(TARGET_DIR))

        for i in tree:
            # print(i)
            allow_types = ['txt','json','py']
            [self.files_location.append(i[0]+'\\'+ele) for ele in i[2] if ele[-len(ele.split('.')[-1]):] in allow_types]
            self.dirs_location.append(i[0])
            all_file_num+=len(i[2])
            all_dir_num+=1

        print('文件數量：',len(self.files_location),'目錄數量：',len(self.dirs_location))

    def replace_key_word_by_filename(self): # 替换文件名
        for i in self.files_location:
            location = i.replace(i.split('\\')[-1],"")
            if KEY_WORD in i.split('\\')[-1]:# 如果存在關鍵詞 ,修改文件名
                print(i)
                os.rename(i,location+i.split('\\')[-1].replace(KEY_WORD,REPLACED_WORD)) # 替换文件名\
                logger.debug(f'{i}替换{KEY_WORD}为{REPLACED_WORD}成功')
                # with open(i,'w+',encoding=ENCODE) as f:
                #     input("是否继续")
                #     result = f.read()
                #     print(result)
                #     f.write(result.replace(KEY_WORD,REPLACED_WORD))
    def replace_key_word_by_content(self):
        # print(__name__)
        # print(self.files_location)
        for i in self.files_location:
            try:
                with open(i,'r',encoding=ENCODE) as f:
                    # print(i)
                    content = f.read()
                    # print(content)
                    if KEY_WORD in content:
                        # print(i)
                        f.close()
                        with open(i,'w',encoding=ENCODE) as w:
                            w.write(content.replace(KEY_WORD,REPLACED_WORD))
                            logger.debug(f"{i}替换{KEY_WORD}为{REPLACED_WORD}成功")
            except Exception as e:
                print(f'ERROR:{e}')

                print(f'出错的文件：{i}')

    def replace_key_word_by_dirname(self):
        for i in sorted(self.dirs_location,key=lambda i:len(i),reverse=True): # Safe List
            last_element = i.split("\\")[-1]
            front_path = i.replace(last_element,'')
            if KEY_WORD in last_element:
                # print(i,front_path+last_element.replace(KEY_WORD,REPLACED_WORD))
                os.rename(i,front_path+last_element.replace(KEY_WORD,REPLACED_WORD))
                logger.debug(f"{i}目录{KEY_WORD}关键词已替换为{REPLACED_WORD}")

if __name__ == '__main__':

    object = catalog_operation()
    # print(object)
    object.replace_key_word_by_content()
    object.replace_key_word_by_filename()
    object.replace_key_word_by_dirname()

