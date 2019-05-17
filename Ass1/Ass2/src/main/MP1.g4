//ID: 1612980
grammar MP;

@lexer::header {
from lexererr import *
}

options{
	language=Python3;
}

program  : mptype 'main' LB RB LP body? RP EOF ;
mptype: INTTYPE | VOIDTYPE ;
body: funcall SEMI;
//2: Program Structure:
program1 : manydecl;

manydecl: onedecl manydecl| onedecl;

onedecl: var_decl_total | func_decl_total | proc_decl_total;

//2.1: Variable declaration:
var_decl_total: 'var' var_decl (SEMI var_decl)* SEMI;

var_decl: list_id COLON type; //vua dinh nghia cho khai bao bien vua la tham so cho func
//list_id???
//type???

//2.2: Function declaration:
func_decl_total: 'function' ID RP (parameter_declaration (SEMI parameter_declaration)*)? RB COLON type SEMI (var_decl_total)? compound_statement;
parameter_declaration: list_id COLON type;
//ID co the sai
//compound-statement???

//2.3: Procedure declaration:
proc_decl_total: 'procedure' ID RP (parameter_declaration (SEMI parameter_declaration)*)? RB SEMI (var_decl_total)? compound_statement;

//3.1: Character Set:

//3.2: Comment:
comment: comment_1|comment_2|comment_3;
comment_1: '(*' (.*)? '*)';
comment_2: LP (.*)? RP;
comment_3: '//' (.*)?;

//3.3: Token Set:

token_set: ID | keywords | operators | separators | literals;

//keywords
keywords: break | continue | for | to | downto | do | if | then | else | return | while | begin | end | function | procedure | var | true | false | array | of | real | boolean | integer | string | not | and | or | div | mod;

break: 'break'| 'BREAK';

continue: 'continue'|'CONTINUE';

for: 'for'|'FOR';

to: 'to'|'TO';

downto: 'downto'|'DOWNTO';

do: 'do'|'DO';

if: 'if'| 'IF';

then: 'then' | 'THEN';

else: 'else' | 'ELSE';

return: 'return' | 'RETURN';

while: 'while' | 'WHILE';

begin: 'begin' | 'BEGIN';

end: 'end'|'END';

function: 'function' | 'FUNCTION';

procedure: 'procedure' | 'PROCEDURE';

var: 'var' | 'VAR';

true: 'true'| 'TRUE';

false: 'false'|'FALSE';

array: 'array'| 'ARRAY';

of: 'of'|'OF';

real: 'real' | 'REAL';

boolean: 'boolean' | 'BOOLEAN';

integer: 'integer' | 'INTEGER';

string: 'string' | 'STRING';

not: 'not' | 'NOT';

and: 'and' | 'AND';

or: 'or' | 'OR';

div: 'div' | 'DIV'; // vua la key vua la operator

mod: 'mod' | 'MOD';

//operators
operators: Add | Mul | NOT | OR | Not_equad | Less_than | Equal | Less_than_equal | Sub | Division | div | Modulus | AND | Greater_than | Greaterthan_equal;

Add: '+';

Mul: '*';

NOT: 'not';

OR: 'or';

Not_equad: '<>';

Less_than: '<';

Equal: '=';

Less_than_equal: Less_than Equal;

Sub: '-';

Division: '/';

Modulus: 'mod';

AND: 'and';

Greater_than: '>';

Greaterthan_equal: Greater_than Equal;

//separators

separators: LSB | RSB | d_dot | comma | LB | RB | SEMI | COLON ;

LSB: '[';

RSB: ']';

d_dot: '..';

comma: ',';

LB: '(' ;

RB: ')' ;

SEMI: ';' ;

COLON: ':';
//literals

literals: integer_type | real_type | boolean_type | string_type;

integer_type: (0|1|2|3|4|5|6|7|8|9)+;

real_type: [0-9]+;

boolean_type: true | false;
exp: funcall | INTLIT ;

funcall: ID LB exp? RB ;

INTTYPE: 'int' ;

VOIDTYPE: 'void'  ;


ID: [a-z A-Z '_'][a-z A-Z '_']* ;

INTLIT: [0-9]+;

LP: '{';

RP: '}';

WS : [ \t\r\n]+ -> skip ; // skip spaces, tabs, newlines


ERROR_CHAR: .;
UNCLOSE_STRING: .;
ILLEGAL_ESCAPE: .;