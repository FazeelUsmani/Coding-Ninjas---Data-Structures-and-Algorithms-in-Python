This folder contains all the solved problems of Huffman Coding
import heapq

class BinaryTreeNode:
    
    def __init__ (self,value,freq):
        self.value=value
        self.freq = freq
        self.left= None
        self.right= None
    def __lt__ (self,other):
        return self.freq<other.freq
    def __eq__ (self,other):
        return self.freq==other.freq
    
class HuffmanCoding:
    
    def __init__ (self,path):
        
        self.path=path
        self.__heap=[]
        self.__codes={}
        self.__reverseCodes={}
        
    def _make_frequency_dict_(self,text):
        
        freq_dict={}
        for char in text:
            if char in freq_dict:
                freq_dict[char]+=1
            else:
                freq_dict[char]=0
    
    def __buildheap(self,freq_dict):
        
        for key in freq_dict:
            
            frequency=freq_dict[key]
            binary_tree_node=BinaryTreeNode(key,frequency)
            heapq.push(self.__heap,binary_tree_node)
    
    def __buildtree():
        while(len(self.__heap)>1):
            binarytreenode1=heapq.heappop(self.__heap)
            binarytreenode2=heapq.heappop(self.__heap)
            freqsum=binarytreenode1.freq + binarytreenode2.freq
            newNode=BinaryTreeNode(None,freqsum)
            newNode.left=binarytreenode1
            newNode.right=binarytreenode2
            heapq.heappush(self.__heap,newNode)
        return
    def buildcodeshelper(self,root,currbits):
        
        if root is None:
            return
        if root.value is not None:
            self.__codes[root.value]=currbits
            self.__reverseCodes[currbits]=root.value
            return
        self.buildcodeshelper(root.left,currbits+'0')
        self.buildcodeshelper(root.right,currbits+'1')
            
    
    def __buildcodes(self):
        root=heapq.heappop(self.__heap)
        self.buildcodeshelper(root,"")
    
    
    def __get_encoded_text(self,text):
        
        encoded_text=""
        for char in text:
            encoded_text+=self.__codes[char]
        return encoded_text
    
    def __paddedEncodedText(self,encoded_text):
        
        paddedamount=8-(len(encoded_text)%8)
        for i in range(paddedamount):
            encoded_text+='0'
        padded_info="{0:08b}".format(paddedamount)
        encoded_text+=padded_info + encoded_text
        return
        
    def __get_bytes_array(self,padded_encoded_text):
        array=[]
        for i in range(0,padded_encoded_text,8):
            byte=padded_encoded_text[i:i+8]
            arr.append(int(byte,2))
        return array
        
        
        
    
    def compress(self):
        filename,file_extension=os.path.splittext(self.path)
        output_path=filename+'.bin'
        
        with open(self.path,'r+') as file, open(output_path,'wb') as output:
        
            text=file.read()
            text=text.rstrip()
            freq_dict=self._make_frequency_dict_(text)
            self.__buildheap(freq_dict)
            self.__buildtree()
            self.__buildcodes()
            encoded_text=self.__get_encoded_text(text)
            padded_encoded_text=self.__get_paddedEncodedText(encoded_text)
            bytes_array=self.__get_bytes_array(padded_encoded_text)
            final_bytes=bytes(bytes_array)
            output.write(final_bytes)
            print('Compressed')
        return 
    
    def __removepadding(self,text):
        paddedinfo=text[:8]
        extrapadding=int(paddedinfo,2)
        text=text[8:]
        final_text_without_padding=text[:-1*extrapadding]
        return final_text_without_padding
    def decodedtext(self,text):
        
        
        decodedtext=""
        currentbits=""
        
        
        for bit in text:
            currentbits+=bit
            if currentbits in self.__reverseCodes:
                character=self.__reverseCodes[currentbits]
                decodedtext+=character
                currentbits=""
            return decodedtext
    
    def decompress(self,input_path):
        filename,file_extension=os.path.splittext(self.path)
        output_path=filename+'decompressed'+'.txt'
        
        with open(input_path,'rb') as file, open(output_path,'w') as output:
                bit_string=""
                byte=file.read(1)
                while byte:
                    byte=ord(byte)
                    bits=bin(byte)[2:].rjust[8:'0']
                    bit_string+=bits
                    byte=file.read(1)
                actual_text=self.__removepadding(bit_string)
                decompressedtext=self.__decodedtext(actual_text)
                output.write(decompressedtext)
        
        
        
        
        
path = 'C:\Users\Younglord\Documents\HuffmanCoding'
h=HuffmanCoding(path)
output_path=h.compress()

h.decompress(output_path)
        
        
        
