//NGUYEN THANH TUAN - 1613907

// array chỗ [0..5] bởi vì m định nghĩa cái float nên nó nhận 0. là float chứ ko nhận ra dc ..
// procedure + funtion cái para  a,b : integer thì nó nhận a,b là 1 token do m ko làm cái list 

grammar MP;

@lexer::header {
from lexererr import *
}

options{
	language=Python3;
}


program  : procedureDeclaration MAIN LB parameterList RB SEMI varDeclarationpart* compoundStatement? ;


body: funcall SEMI;

funcall: ID LB (exp (COMMA exp)*)? RB ;

//INTTYPE: 'int' ;

VOIDTYPE: 'void'  ;

LP: '{';

RP: '}';

ASSIGN : ':=';

WS : [ \t\r\n]+ -> skip ; // skip spaces, tabs, newlines



//VAR DECLARATION : 

IDList : ID (COMMA ID)* ;

varDeclarationpart: VAR varDeclaration (SEMI varDeclaration)* SEMI ;

varDeclaration : IDList COLON mptype  ;

//FUNCTION DECLARATION

functionDeclaration : FUNCTION ID LB (parameterList)? RB COLON resultType SEMI (varDeclarationpart)? compoundStatement ;

parameterList : parameterDeclaration (SEMI parameterDeclaration)* ;

parameterDeclaration : IDList COLON resultType;

resultType : mptype | ctype ;

identifier : ID;

statements : statement (SEMI statement)* ;

statement :  ifStatement | forStatement | whileStatement | compoundStatement | withStatement 
			| hi ;
hi : assignmentStatement | breakStatement | continueStatement | RETURN | callStatement SEMI ;	

//PROCEDURE DECLARATION : 

procedureDeclaration : PROCEDURE ID LB (parameterList)? RB  SEMI (varDeclarationpart)? compoundStatement ;

//CHARACTER SET


//FRAGMENT :

//fragment ESC: '\\' [bfrnt'"\\] ;
 //khi gap 1 dau thi no se bo qua



//KEYWORDS : 
 
WITH : W I T H ;
  
BREAK : B R E A K ;
 
CONTINUE : C O N T I N U E ; 

FOR : F O R ;

TO : T O ;

DOWNTO : D O W N T O ;

DO : D O ;

IF : I F ;

THEN : T H E N ;

ELSE : E L S E ;

RETURN : R E T U R N ;

WHILE : W H I L E ;

BEGIN : B E G I N ;

END : E N D ;

FUNCTION : F U N C T I O N ;

PROCEDURE : P R O C E D U R E ;

VAR : V A R ;

TRUE : T R U E ;

FALSE : F A L S E ;

ARRAY :A R R A Y ;

OF : O F ;

REAL : R E A L ;

BOOLEAN : B O O L E A N ;

INTEGER : I N T E G E R ;

STRING : S T R I N G ;

NOT : N O T ;

AND : A N D ;

OR : O R ;

DIV : D I V ;

MOD : M O D ;

MAIN : M A I N;

//OPERATORS :

 PLUS : '+';
 
 STAR : '*';
 
 NOTEQUAL : '<>';
 
 LT : '<';
 
 LE : '<=';
 
 MINUS : '-';
 
 DIVISION : '/';
 
 EQUAL : '=';
 
 GT : '>';
 
 GE : '>=';
 

 //SEPARATORS :
 
 LSB : '[';

 RSB : ']';
 
 COLON: ':';
 
 LB: '(' ;

 RB: ')' ;
 
 SEMI: ';' ;
 
 DOTDOT : '..';
 
 COMMA: ',';
 
//COMMENTS
  COMMENT_1 : '(*' .*? '*)' -> skip ;
  
  COMMENT_2 : '/*' .*? '*/' ->skip ;

  LINE_CMT  : '//' ~[\r\n]* ->skip;

//IDENTIFIERS : 

 ID:[_a-zA-Z][_a-zA-Z0-9]*;

//LITERALS : 
 
 INTLIT: [0-9]+;
 
 BOOLLIT : TRUE | FALSE ;
 
 FLOATLIT     
    : DIGIT+ '.'? (DIGIT* (EXPONENT)?)?
    |'.' DIGIT+ EXPONENT?
    | DIGIT EXPONENT
    ;

fragment DIGIT: [0-9]+ ;

fragment EXPONENT: ('e'|'E') ('-')? [0-9]+;
 
fragment STRING_QUOTE : '"' (~('\''|'\\'))* '"';

 STRING_LIT: STRING_QUOTE { self.text = self.text[1:-1] } ;

//TYPES AND VALUES : 

mptype: INTTYPE | BOOLEANTYPE | REALTYPE | STRINGTYPE | VOIDTYPE ;
 
 BOOLEANTYPE: BOOLLIT;
 
 INTTYPE : INTLIT;
 
 REALTYPE : FLOATLIT;
 
 STRINGTYPE: STRING_LIT;
 
 ctype: ARRAY LSB index RSB OF mptype ;
  
 index : INTLIT DOTDOT INTLIT ;
 
//EXPRESSIONS : 

//exp: funcall | INTLIT ;
exp : simpleexp | simpleexp (relationaloperator exp)? ;

simpleexp : term (additiveoperator simpleexp)? ;

additiveoperator
   : PLUS
   | MINUS
   | OR
   ;
term
   : signedFactor (multiplicativeoperator term)?
   ; 
relationaloperator
   : EQUAL
   | NOTEQUAL
   | LT
   | LE
   | GE
   | GT
   ;
 multiplicativeoperator
   : STAR
   | OR
   | PLUS
   | MINUS
   ;
   
 signedFactor : (PLUS|MINUS)? factor ;
 
 factor 
    : variable
   | LP exp RP
   | functionDesignator
   | unsignedConstant
   | NOT factor
   | BOOLLIT
   ;
   
  
functionDesignator
   : 
   LP parameterList RP
   ;

unsignedConstant
   : unsignedNumber
   | STRING_LIT
   ;

unsignedNumber
   : unsignedInteger
   | unsignedReal
   ;

unsignedInteger
   : INTLIT
   ;

unsignedReal
   : FLOATLIT
   ;

elementList
   : element (COMMA element)*
   |
   ;

element
   : exp (DOTDOT exp)?
   ;

//(LB exp (COMMA exp)* RB | LB2 exp (COMMA exp)* RB2 | DOT identifier | POINTER)*;
   variable
   : ID | ID exp ;
  
//ASSIGNMENT STATEMENT : 

 assignmentStatement : variableAssign ASSIGN exp ;

variableAssign: ID ASSIGN variableAssign | ID ASSIGN ;

//THE IF STATEMENT :
 
 ifStatement : IF exp THEN  statements (ELSE statements)? ;

//THE WHILE STATEMENT :

 whileStatement : WHILE exp DO statements ;

//THE FOR STATEMENT :

forStatement : ID  ASSIGN  exp (TO|DOWNTO) exp DO statements ;

//THE BREAK STATEMENT :

breakStatement : BREAK SEMI ;

//THE CONTINUE STATEMENT :

continueStatement : CONTINUE SEMI ;

//THE COMPOUND STATEMENT :

compoundStatement : BEGIN (statements)? END ;

//THE WITH STATEMENT :

withStatement : WITH varDeclarationpart+ SEMI DO statement ;

//THE CALL STATEMENT :

callStatement : ID  exp (:exp)* RB ;


fragment A : ('a'|'A');
fragment B : ('b'|'B');
fragment C : ('c'|'C');
fragment D : ('d'|'D');
fragment E : ('e'|'E');
fragment F : ('f'|'F');
fragment G : ('g'|'G');
fragment H : ('h'|'H');
fragment I : ('i'|'I');
fragment J : ('g'|'J');
fragment K : ('k'|'K');
fragment L : ('l'|'L');
fragment M : ('m'|'M');
fragment N : ('n'|'N');
fragment O : ('o'|'O');
fragment P : ('p'|'P');
fragment Q : ('q'|'Q');
fragment R : ('r'|'R');
fragment S : ('s'|'S');
fragment T : ('t'|'T');
fragment U : ('u'|'U');
fragment V : ('v'|'V');
fragment W : ('w'|'W');
fragment X : ('x'|'X');
fragment Y : ('y'|'Y');
fragment Z : ('z'|'Z');


 
ERROR_CHAR
    : .
        { 
            raise ErrorToken(self.text) 
        }
    ;
ILLEGAL_ESCAPE
    : '"' (ESC | ~["\\])*? ([\\] ~[bfrnt'"\\]) 
        {
           raise IllegalEscape(self.text[1:])
        }
        //(ESC | ~[\r\n] )*  '"'
    ;

UNCLOSE_STRING
    :  '"' (ESC | ~["\r\n] |((~'\\')'\\"'))* ('\n'| EOF)
        {
            if self.text[-1]=='\n':
                 raise UncloseString(self.text[1:-1])
            else:
                raise UncloseString(self.text[1:])
        }
    ;





 
 
