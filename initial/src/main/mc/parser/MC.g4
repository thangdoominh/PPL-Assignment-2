/**
*   Student's Name    : Do Minh Thang
*   Student's ID      : 1713217
**/

grammar MC;

@lexer::header {
from lexererr import *
}

@lexer::member {
def emit(self):
	tk = self.type
	if tk == UNCLOSE_STRING:
		result = super.emit();
		raise UncloseString(result.text[1:]);
	elif tk == ILLEGAL_ESCAPE:
		result = super.emit();
		raise IllegalEscape(result.text[1:]);
	elif tk == ERROR_CHAR:
		result = super.emit();
		raise ErrorToken(result.text);
	else:
		return super.emit();
}

options{
	language=Python3;
}

program : declaration+ EOF
		;

declaration
		: vardeclaration
		| funcdeclaration
		;
// vardeclaration
vardeclaration
		: singletype idlist SEMI
        ;
singletype
		: INTTYPE
		| FLOATTYPE
		| BOOLTYPE
		| STRINGTYPE
		;
idlist
		: idtail (COMMA idtail)*
		;
idtail
		: idarray
		| idsingle
		;
idarray
		: ID LSB INTLIT RSB
		;
idsingle
		: ID
		;

// funcdeclaration
funcdeclaration
		: (singletype | VOIDTYPE | arraypointertype) ID LB paralist_decla? RB  block
		;
paralist_decla
		: paradecla (COMMA paradecla)*
		;
paradecla
		: singletype idsingle (LSB RSB)?
		;
arraypointertype
		: singletype LSB RSB ;
block
		: LP (vardeclaration | statement)* RP
		;
statement
		: ifstmt
		| dowhilestmt
		| forstmt
		| breakstmt
		| continuestmt
		| returnstmt
		| expressionstmt
		| block
		;
ifstmt
		: IF LB expression RB statement (ELSE statement)?
		;
dowhilestmt
		: DO statement+ WHILE expression SEMI
		;
forstmt
		: FOR LB expression SEMI expression SEMI expression RB statement
		;
// BREAK chỉ xuất hiện trong vòng lập for và do while
breakstmt
		: BREAK SEMI
		;
// CONTINUE chỉ xuất hiện trong vòng lập for và do while
continuestmt
		: CONTINUE SEMI
		;
returnstmt
		: RETURN expression? SEMI
		;
expressionstmt
		: expression SEMI
		;
expression
		: exp1 ASSIGN_OP expression
		| exp1
		;
exp1
		: exp1 OR_OP exp2
		| exp2
		;
exp2
		: exp2 AND_OP exp3
		| exp3
		;
exp3
		: exp4 (EQUAL_OP | NOT_EQUAL_OP) exp4
		| exp4
		;
exp4
		: exp5 (LESS_OP | LESS_EQUAL_OP | GREATER_OP | GREATER_EQUAL_OP) exp5
		| exp5
		;
exp5
		: exp5 (ADD_OP | SUB_OP) exp6
		| exp6
		;
exp6
		: exp6 (DIV_OP | MUL_OP | MOD_OP) exp7
		| exp7
		;
exp7
		: (SUB_OP | NOT_OP) exp7
		| exp8
		;
exp8
		: exp9 LSB expression RSB
		| exp9
		;
exp9
		: LB expression RB
		| exp10
		;
exp10
		: operand
		| funccall
		;
operand
		: INTLIT
		| FLOATLIT
		| STRINGLIT
		| BOOLLIT
		| ID
		;
funccall
		: ID LB paralist_call? RB
		;
paralist_call
		: para_call (COMMA para_call)*
		;
para_call
		: operand
		| expression
		;
BOOLLIT     : TRUE
			| FALSE
			;
INTLIT      : [0-9]+;

FLOATLIT    : FRAC
			| EXPONENT
			;

FRAC        : INTLIT?'.'INTLIT
			| INTLIT'.'INTLIT?
			;

EXPONENT    : (FRAC|INTLIT)[eE][-]?INTLIT ;
// Type value
INTTYPE     : 'int';
BOOLTYPE    : 'boolean';
STRINGTYPE  : 'string';
FLOATTYPE   : 'float';
VOIDTYPE    : 'void';

// 3.3 Token Set
// a. Identifiers

// b. Keywords
BREAK       : 'break';
CONTINUE    : 'continue';
RETURN      : 'return';
ELSE        : 'else';
FOR         : 'for';
IF          : 'if';
DO          : 'do';
WHILE       : 'while';
TRUE        : 'true';
FALSE       : 'false';

ID          : [_a-zA-Z][_a-zA-Z0-9]*;

// c. Operators
ADD_OP              : '+';
SUB_OP              : '-';
MUL_OP              : '*';
DIV_OP              : '/';
NOT_OP              : '!';
MOD_OP              : '%';
OR_OP               : '||';
AND_OP              : '&&';
NOT_EQUAL_OP        : '!=';
EQUAL_OP            : '==';
LESS_OP             : '<';
GREATER_OP          : '>';
LESS_EQUAL_OP       : '<=';
GREATER_EQUAL_OP    : '>=';
ASSIGN_OP           : '=';

// 3.4 Separators
LSB     : '[';
RSB     : ']';
LP      : '{';
RP      : '}';
LB      : '(';
RB      : ')';
SEMI    : ';';
COMMA   : ',';

// 3.5 Literals


WS          : [ \b\f\t\r\n] -> skip ;
STRINGLIT   :'"' ('\\' [bfrnt"\\] | ~[\b\f\r\n\t"\\] )* '"'
			{
				self.text = self.text[1:-1]
			}
			;
COMMENTS_LINE   : '//' ~[\n\r\t\f]* -> skip;
COMMENTS_BLOCK  : '/*' .*? '*/' -> skip;
ILLEGAL_ESCAPE  : '"'(~[\n"\\] | '\\' [bfrtn"\\])* ('\\' ~[bnrft"])
				{
					raise IllegalEscape(self.text[1:])
				}
				;
UNCLOSE_STRING  : '"' ( ~[\b\f\r\t\n"\\] | '\\' [bfrnt"\\])*
				{
					raise UncloseString(self.text[1:])
				}
				;
ERROR_CHAR      :.
				{
					raise ErrorToken(self.text)
				}
				;
