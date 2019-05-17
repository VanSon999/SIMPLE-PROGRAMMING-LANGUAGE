grammar MP;

@lexer::header {
1552286
from lexererr import *
}

options{
	language=Python3;
}






//Comment

CMT: ('(*'.*?'*)' | '{'.*?'}' | '//' ~[\r\n]*)  -> skip ;

//Keyword

REALTYPE: [rR][eE][aA][lL]; 

BREAK: [bB][rR][eE][aA][kK];

CONTINUE: [cC][oO][nN][tT][iI][nN][uU][eE];

FOR: [fF][oO][rR];

TO: [tT][oO];

DOWNTO: [dD][oO][wW][nN][tT][oO];

WITH: [wW][iI][tT][hH];

DO: [dD][oO];

IF: [iI][fF];

THEN: [tT][hH][eE][nN];

ELSE: [eE][lL][sS][eE];

RETURN: [rR][eE][tT][uU][rR][nN];

WHILE: [wW][hH][iI][lL][eE];

BEGIN: [bB][eE][gG][iI][nN];

END: [eE][nN][dD];

FUNCTION: [fF][uU][nN][cC][tT][iI][oO][nN];

PROCEDURE: [pP][rR][oO][cC][eE][dD][uU][rR][eE];

VAR: [vV][aA][rR];

fragment TRUE: [tT][rR][uU][eE];

fragment FALSE: [fF][aA][lL][sS][eE];

ARRTYPE: [aA][rR][rR][aA][yY];

OF: [oO][fF];

BOOLEAN: [bB][oO][oO][lL][eE][aA][nN];

INTTYPE: [iI][nN][tT][eE][gG][eE][rR];

STRING: [sS][tT][rR][iI][nN][gG];

ADDOP: '+';

MULOP: '*';

NOTOP: [nN][oO][tT];

OROP: [oO][rR];

NOEQOP: '<>';

LSOP: '<';

LSEQOP: '<=';

DIVOP: [dD][iI][vV];

SUBOP: '-';

FDIVOP: '/';

MODOP: [mM][oO][dD];

ANDOP: [aA][nN][dD];

EQOP: '=';

GTOP: '>';

GTEQOP: '>=';

ID: [_a-zA-Z][_0-9a-zA-Z]*;

//Datatype



INTLIT: [0-9]+;

REALLIT: [0-9]*'.'?[0-9]+([eE][-+]?[0-9]+)?;

BOOLLIT: TRUE | FALSE ;

fragment ESC: '\\' [bfrnt'"\\];

STR:  '"'(ESC | ~('\n' | [\\"]))* '"'{self.text = self.text.replace('"','')};

//separators 
ASSI: ':=';

LS:'[';

RS:']';

LB: '(' ;

RB: ')' ;

COLO: ':';

CM: ',';

DD: '..';


SEMI: ';';


// ----------- PARSER --------------------


program  : dec* EOF ;
//decleration
dec : vardec | fundec | prodec;

vardec : VAR vdecs+ ;

vdecs: listid COLO kind SEMI ;

listid: ID (CM ID)*;

kind: arr | manytype;

arr: ARRTYPE LS exp DD exp RS OF manytype ; 

manytype: INTTYPE | REALTYPE |BOOLEAN | STRING;

datatype: INTLIT | REALLIT | BOOLLIT | STR;
fundec: FUNCTION ID LB listpara? RB COLO kind SEMI  vardec? compstt ;

listpara: para (SEMI para)*  ;

para: listid COLO kind;

prodec: PROCEDURE ID LB listpara? RB SEMI  vardec? compstt;


//statement
sttment: assiment | ifstt | whilestt | forstt | breakstt | contistt | retstt | compstt | widostt | callstt  ; 

assiment : ( ( ID | index | funcall ) ASSI )+ exp SEMI;

ifstt: IF exp THEN sttment (ELSE sttment)? ;

whilestt: WHILE exp DO sttment;

forstt: FOR ID ASSI exp (TO | DOWNTO) exp DO sttment;



breakstt: BREAK SEMI;

contistt: CONTINUE SEMI;

retstt: RETURN (exp)? SEMI;

compstt: BEGIN sttment* END;

widostt: WITH vdecs+ DO sttment ;

funcall: ID LB listexp? RB ;

callstt: ID LB listexp? RB SEMI;

listexp: exp (CM exp)* ;

index: (ID | funcall) LS exp RS;

//Expression
exp: LB exp RB
	| <assoc=right>	 (NOTOP | SUBOP) exp 

	| exp (FDIVOP |MULOP |  DIVOP | MODOP | ANDOP ) exp

	| exp (ADDOP | SUBOP | OROP ) exp

	| exp1 (EQOP | NOEQOP | LSOP | LSEQOP | GTOP | GTEQOP ) exp1

 	| exp (ANDOP  THEN | OROP ELSE) exp  

	| ID | datatype | index |funcall ;

exp1: index | funcall | ID | INTLIT | REALLIT | BOOLLIT | LB exp RB ;

/*exp : exp (ANDOP THEN | OROP ELSE) exp1 | exp1;

exp1 : exp2 (EQOP | NOEQOP | LSOP | LSEQOP | GTOP | GTEQOP ) exp2 | exp2;

exp2:  exp2 (ADDOP | SUBOP | OROP ) exp3 | exp3 ;

exp3: exp3 (FDIVOP |MULOP |  DIVOP | MODOP | ANDOP ) exp4 | exp4;

exp4: (NOTOP | SUBOP) exp4 | exp5;

exp5:  index | funcall | ID | INTLIT | REALLIT | BOOLLIT | LB exp RB ; */

WS : [ \t\r\n]+ -> skip ; // skip spaces, tabs, newlines


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
