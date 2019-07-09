class Mydb(object):
    
    def open_file(self):
        self.fp = open('info.json', 'w', encoding='utf-8')
        print('打开文件')

    def close_file(self):
        self.fp.close()
        print('关闭文件')

    def save_as_json(self, item):
        item_dict = item.__dict__
        self.fp.write(str(item_dict)+'\n')