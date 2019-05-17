Set environment variable ANTLR_LIB to the file antlr-4.7.1-complete.jar in your computer
Change current directory to initial/src where there is file run.py
Type: python3 run.py gen 
Then type: python3 run.py test LexerSuite
Then type: python3 run.py test ParserSuite
Then type: python3 run.py test ASTGenSuite
Then type: python3 run.py test CheckSuite
Then type: python3 run.py test CodeGenSuite

cd /usr/local/lib


sudo wget https://www.antlr.org/download/antlr-4.7.1-complete.jar
thêm dòng này vào cuối file 
nano ~/.bashrc

ANTLR_LIB='/usr/local/lib/antlr-4.7.1-complete.jar'
export ANTLR_LIB

sudo apt-get update
sudo apt install -y build-essential
sudo apt-get install python3-pip
sudo pip3 install antlr4-python3-runtime



bai 1:
ID: [a-z][0-9a-z]* ;
bai 2:
fragment Letter: [a-z];
fragment Number: [0-9];
ID: Letter(Number|Letter)* ;
bai 3a:
fragment Letter: [a-z];
fragment Number: [0-9];
REAL: Number+'.'?Number*'e'?'e-'?Number+;


//trong python "string" : /" = "

my computer::
cd /mnt/c/Users/VanSon/Desktop/PPL/Assignment_1/Ass2
export ANTLR_LIB=/mnt/c/Users/VanSon/Desktop/PPL/antlr-4.7.1-complete.jar
export ANTLR_LIB=/mnt/c/Users/VanSon/Desktop/PPL/Assignment_2/antlr-4.7.1-complete.jar
echo $ANTLR_LIB

cd src

python3 run.py gen
python3 run.py test LexerSuite
python3 run.py test ParserSuite

//dung phan mem de ve cay parse tree dung de test
- B1: cai java jdk
- B2: comment mot so phan python trong file MP.g4
- B3: python3 run.py gen 
- B4: go javac -cp $ANTLR_LIB ../target/main/mc/parser/*.java
- B5: go javac -cp $ANTLR_LIB:../target/main/mc/parser/org.antlr.v4.gui.TestRing MP program -gui test/testcases/202.txt //co the chon file khac fie 202.txt
co the sua program -> expression

# phai dao, trai k da
#dung khi van pham duoi dang bnef
# tl = ctx.term()[::-1]
# ol = ctx.ASSIGN()[::-1]
# return reduce(lambda x,y: Binary(y[1].getText(),self.visit(y[0]),x),zip(tl[1:],ol),self.visit(tl[0]))

intelide