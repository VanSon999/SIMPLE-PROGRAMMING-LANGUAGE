//Họ và tên: Nguyễn Văn Sơn
//ID: 1612980

grammar MP;

@lexer::header {
from lexererr import *
}

options{
	language=Python3;
}

//program  : mptype 'main' LB RB LP body? RP EOF ;

//mptype: INTTYPE | VOIDTYPE ;

//body: funcall SEMI;

//exp: funcall | INTEGER_TYPE ;

//funcall: ID LB exp? RB ;

//INTTYPE: 'int' ;

//VOIDTYPE: 'void'  ;

//ID: [a-zA-Z]+ ;

//////////////////////////////////////////////Parser/////////////////////////////////////////////
program : decl* EOF;
decl: var_decl_total | func_decl_total | proc_decl_total;
//2.1: Variable declaration:
var_decl_total: VAR var_decl+;

// var_decl: list_id COLON (type_data | type_array) SEMI;
var_decl: IDENTIFIER (COMMA IDENTIFIER)* COLON (type_data | type_array) SEMI;
// list_id: IDENTIFIER (COMMA IDENTIFIER)*;  //////// can kiem tra lai0

type_data: INTEGER | REAL | BOOLEAN | STRING; //////// can kiem tra lai

// type_array: ARRAY (LSB exp D_DOT exp RSB)? OF type_data;
type_array: ARRAY LSB SUB? INTEGER_TYPE D_DOT SUB? INTEGER_TYPE RSB OF type_data;
//2.2: Function declaration:
func_decl_total: FUNCTION IDENTIFIER LB list_parameter? RB COLON (type_data | type_array) SEMI (var_decl_total)? compound_statement;
list_parameter: parameter (SEMI parameter)*; 
parameter: IDENTIFIER (COMMA IDENTIFIER)* COLON (type_data | type_array);
//parameter: list_id COLON (type_data | type_array);
//2.3: Procedure declaration:
proc_decl_total: PROCEDURE IDENTIFIER LB list_parameter? RB SEMI (var_decl_total)? compound_statement;

//6.Statements and Control Flow:
statement: assignment_statement | if_statement | for_statement | while_statement | break_statement | continue_statement | return_statement | func_call_statement | compound_statement | with_statement;

//6.1 assignment Statement - can kiem tra
// assignment_statement: ((IDENTIFIER|index_express) ASSIGN)+ exp SEMI;
assignment_statement: (lhs_assign ASSIGN)+ exp SEMI;

lhs_assign: IDENTIFIER|index_express;
//6.2 The if Statement
if_statement: IF exp THEN statement (ELSE statement)?;

//6.3 The while Statement
while_statement: WHILE exp DO statement;

//6.4 The for Statement 
for_statement: FOR IDENTIFIER ASSIGN exp (TO | DOWNTO) exp DO statement;

//6.5 The break Statement
break_statement: BREAK SEMI;

//6.6 The continue Statement
continue_statement: CONTINUE SEMI;

//6.7 The return Statement
return_statement: RETURN exp? SEMI;

//6.8 The compound Statement
compound_statement: BEGIN statement* END;

//6.9 The with statement
with_statement: WITH var_decl+ DO statement;
//6.10 Call statement
func_call_statement: IDENTIFIER LB list_exp? RB SEMI ; // can xem lai

list_exp: exp (COMMA exp)*;

//5.Expression
//5.1: Precedence and Associativity:
exp: exp AND THEN exp1 | exp OR ELSE exp1 | exp1;  
exp1: exp2 EQUAL exp2 | exp2 NOT_EQUAD exp2 | exp2 LESS_THAN exp2 | exp2 LESS_THAN_EQUAL exp2 | exp2 GREATER_THAN exp2 | exp2 GREATER_THAN_EQUAL exp2 | exp2;
exp2: exp2 ADD exp3 | exp2 SUB exp3 | exp2 OR exp3 | exp3;
exp3: exp3 DIVISION exp4 | exp3 MUL exp4 | exp3 DIV exp4 | exp3 MOD exp4 | exp3 AND exp4 | exp4;
exp4: NOT exp4 | SUB exp4 | exp5;
exp5: literal | IDENTIFIER | func_call | LB exp RB | index_express; // con thieu??? element of an array or a function call.


//exp5: operand LSB exp RSB | operand
//operand: LB exp RB| literal | funcall | IDENTIFIER
//5.3: Index Expression
// index_express: (IDENTIFIER| func_call) LSB exp? RSB;
index_express: (IDENTIFIER| func_call) LSB exp RSB;
func_call: IDENTIFIER LB list_exp? RB;
//index_express: exp LSB exp RSB;
//////////////////////////////////////////////Lexer////////////////////////////////////////////


//3.1 Character set:
fragment A: ('a'|'A');
fragment B: ('b'|'B');
fragment C: ('c'|'C');
fragment D: ('d'|'D');
fragment E: ('e'|'E');
fragment F: ('f'|'F');
fragment G: ('g'|'G');
fragment H: ('h'|'H');
fragment I: ('i'|'I');
fragment J: ('j'|'J');
fragment K: ('k'|'K');
fragment L: ('l'|'L');
fragment M: ('m'|'M');
fragment N: ('n'|'N');
fragment O: ('o'|'O');
fragment P: ('p'|'P');
fragment Q: ('q'|'Q');
fragment R: ('r'|'R');
fragment S: ('s'|'S');
fragment T: ('t'|'T');
fragment U: ('u'|'U');
fragment V: ('v'|'V');
fragment W: ('w'|'W');
fragment X: ('x'|'X');
fragment Y: ('y'|'Y');
fragment Z: ('z'|'Z');

//KEYWORKS: BREAK | CONTINUE | FOR | TO | DOWNTO | DO | IF | THEN | ELSE | WHILE | BEGIN | END | FUNCTION | PROCEDURE | VAR | TRUE | FALSE | ARRAY | OF | REAL | BOOLEAN | INTEGER | STRING | NOT | AND | OR | DIV | MOD | RETURN;

BREAK: B R E A K;

CONTINUE: C O N T I N U E;

FOR: F O R;

TO: T O;

DOWNTO: D O W N T O;

DO: D O;

IF: I F;

THEN: T H E N;

ELSE: E L S E;

WHILE: W H I L E;

BEGIN: B E G I N;

END: E N D;

FUNCTION: F U N C T I O N;

RETURN: R E T U R N;

PROCEDURE: P R O C E D U R E;

VAR: V A R;

TRUE: T R U E;

FALSE: F A L S E;

ARRAY: A R R A Y;

OF: O F;

REAL: R E A L; 

BOOLEAN: B O O L E A N;

INTEGER: I N T E G E R;

STRING: S T R I N G;

NOT: N O T;

AND: A N D;

OR: O R;

DIV: D I V; // vua la key vua la operator

MOD: M O D;

//OPERATORS: ADD | MUL | NOT | OR | NOT_EQUAD | LESS_THAN | EQUAL | LESS_THAN_EQUAL| SUB | DIVISION | DIV | MODULUS | AND | GREATER_THAN | GREATER_THAN_EQUAL;

ADD: '+';

MUL: '*';

NOT_EQUAD: '<>';

LESS_THAN: '<';

EQUAL: '=';

LESS_THAN_EQUAL: LESS_THAN EQUAL;

SUB: '-';

DIVISION: '/';

MODULUS: M O D;

GREATER_THAN: '>';

GREATER_THAN_EQUAL: GREATER_THAN EQUAL;

WITH: W I T H;

//3.3_separators

//SEPARATORS: LSB | RSB | D_DOT | COMMA | LB | RB | SEMI | COLON ;

LSB: '[';

RSB: ']';

D_DOT: '..';

COMMA: ',';

COLON: ':';

//phan them:
ASSIGN: ':=';
LB: '(' ;

RB: ')';

SEMI: ';' ;

//3.2_Comment:
// COMMENT: COMMENT_1|COMMENT_2|COMMENT_3;
COMMENT_1: '(*' .*? '*)' -> skip;
COMMENT_2: '{' .*? '}' -> skip;
COMMENT_3: '//' ~[\r\n]* ->skip;

//COMMENT: (('(*' .*? '*)') | ('{' .*? '}') | ('//' .*?)) -> skip;

//3.3_identifiers:
IDENTIFIER: CHARACTER (CHARACTER | INTEGER_TYPE)* ;
fragment CHARACTER: A | B | C | D | E | F | G | H | I | J | K | L | M | N | O | P | Q | R | S | T | U | V | W | X | Y | Z | '_'; 
//3.5_Literals:

literal: INTEGER_TYPE | REAL_TYPE | boolean_type | STRINGLIT;

INTEGER_TYPE: [0-9]+;

// REAL_TYPE: INTEGER_TYPE (('.' INTEGER_TYPE (EXPONENT)?)? | EXPONENT);

// fragment EXPONENT: E ('+' | '-')? INTEGER_TYPE;
REAL_TYPE: (INTEGER_TYPE '.' ([0-9]+)? | '.' ([0-9]+) ) EXPONENT? | INTEGER_TYPE EXPONENT;

fragment EXPONENT: E ('-')? INTEGER_TYPE;


boolean_type: TRUE | FALSE;

STRINGLIT
    : '"' STRING_S* '"' 
        {
            self.text = self.text[1:-1]
        }
    ;
WS : [ \t\r\n]+ -> skip ; // skip spaces, tabs, newlines
fragment STRING_S: ~["\\\n\r] | ESC;
fragment ESC
		: '\\' [btnfr"'\\]; //khi gap 1 dau \ thi no se bo qua

ERROR_CHAR
    : .
        { 
            raise ErrorToken(self.text) 
        }
    ;

ILLEGAL_ESCAPE
    : '"' STRING_S* '\\' ~[btnfr"'\\]
        {
           raise IllegalEscape(self.text[1:])
        }
        //(ESC | ~[\r\n] )*  '"'
        
    ;

UNCLOSE_STRING
    :  '"' STRING_S*
        {
                raise UncloseString(self.text[1:])
        }
    ;