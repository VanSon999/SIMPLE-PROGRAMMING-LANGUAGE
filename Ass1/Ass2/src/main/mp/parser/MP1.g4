grammar MP;
//ID: 1612980
@lexer::header {
from lexererr import *
}

options{
	language=Python3;
}

// program  : mptype 'main' LB RB LP body? RP EOF ;

// mptype: INTTYPE | VOIDTYPE ;

// body: funcall SEMI;

// exp: funcall | INTLIT ;

// funcall: ID LB exp? RB ;

// INTTYPE: 'int' ;

// VOIDTYPE: 'void'  ;

// ID: [a-zA-Z]+ ;

INTLIT: [0-9]+;

// LB: '(' ;

// RB: ')' ;

// LP: '{';

// RP: '}';

// SEMI: ';' ;

// WS : [ \t\r\n]+ -> skip ; // skip spaces, tabs, newlines

program : manydecl;

manydecl: onedecl manydecl| onedecl;

onedecl: var_decl_total | func_decl_total | proc_decl_total;

//2.1: Variable declaration:
var_decl_total: 'var' var_decl (SEMI var_decl)* SEMI;

var_decl: list_id COLON type;

list_id: IDENTIFIER (COMMA IDENTIFIER)*;  //////// can kiem tra lai

type: INTEGER_TYPE | REAL_TYPE | BOOLEAN_TYPE | STRINGLIT; //////// can kiem tra lai

//2.2: Function declaration:
func_decl_total: FUNCTION IDENTIFIER LB (parameter_declaration (SEMI parameter_declaration)*)? RB COLON type SEMI (var_decl_total)? compound_statement;
parameter_declaration: list_id COLON type;

//2.3: Procedure declaration:
proc_decl_total: PROCEDURE IDENTIFIER LB (parameter_declaration (SEMI parameter_declaration)*)? RB SEMI (var_decl_total)? compound_statement;

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

//3.3_keywords
keywords: BREAK | CONTINUE | FOR | TO | DOWNTO | DO | IF | THEN | ELSE | WHILE | BEGIN | END | FUNCTION | PROCEDURE | VAR | TRUE | FALSE | ARRAY | OF | REAL | BOOLEAN | INTEGER | STRING | NOT | AND | OR | DIV | MOD | RETURN;

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

//3.3_operators
operators: ADD | MUL | NOT | OR | NOT_EQUAD | LESS_THAN | EQUAL | LESS_THAN_EQUAL| SUB | DIVISION | DIV | MODULUS | AND | GREATER_THAN | GREATER_THAN_EQUAL;

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

//3.3_separators

separators: LSB | RSB | D_DOT | COMMA | LB | RB | SEMI | COLON ;

LSB: '[';

RSB: ']';

D_DOT: '..';

COMMA: ',';

LB: '(' ;

RB: ')' ;

SEMI: ';' ;

COLON: ':';

//phan them:
LP: '{';

RP: '}';

ASSIGN: ':=';
//3.2_Comment:
COMMENT: COMMENT_1|COMMENT_2|COMMENT_3;
COMMENT_1: '(*' (.*?) '*)';
COMMENT_2: '{' (.*?) '}';
COMMENT_3: '//' (.*?);

//3.3_identifiers:
IDENTIFIER: CHARACTER (CHARACTER | INTLIT)* ;
CHARACTER: A | B | C | D | E | F | G | H | I | J | K | L | M | N | O | P | Q | R | S | T | U | V | W | X | Y | Z | '_'; 
//3.5_Literals:

LITERAL: INTEGER_TYPE | REAL_TYPE | EXPONENT | BOOLEAN_TYPE | STRINGLIT;

INTEGER_TYPE: INTLIT+;

REAL_TYPE: INTLIT+ (('.' INTLIT+ (EXPONENT)?)? | EXPONENT);

EXPONENT: ('e') ('+' | '-')? INTLIT+;

BOOLEAN_TYPE: 'true' | 'false';

STRINGLIT: '"' (~["\\\n\r] | EscapeSequence)* '"';

fragment EscapeSequence: '\\' [btnfr"'\\];

//4.


//5.Expression
//5.1: Precedence and Associativity:
exp: exp AND THEN exp1 | exp OR ELSE exp1 | exp1;  
exp1: exp2 EQUAL exp2 | exp2 NOT_EQUAD exp2 | exp2 LESS_THAN exp2 | exp2 LESS_THAN_EQUAL exp2 | exp2 GREATER_THAN exp2 | exp2 GREATER_THAN_EQUAL exp2 | exp2;
exp2: exp2 ADD exp3 | exp2 SUB exp3 | exp2 OR exp3 | exp3;
exp3: exp3 DIVISION exp4 | exp3 MUL exp4 | exp3 DIV exp4 | exp3 MOD exp4 | exp3 AND exp4 | exp4;
exp4: NOT exp4 | SUB exp4 | exp5;
exp5: LITERAL | IDENTIFIER ; // con thieu??? element of an array or a function call.


//6.Statements and Control Flow:

//6.1: Assignment Statement:


//6.2: The if Statement:
	
//6.8: The compound Statement:
compound_statement: BEGIN Statement END;

ERROR_CHAR: .;
UNCLOSE_STRING: .;
ILLEGAL_ESCAPE: .;