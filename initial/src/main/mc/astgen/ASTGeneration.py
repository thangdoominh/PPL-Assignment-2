#
#   Student's Name    : Do Minh Thang
#   Student's ID      : 1713217
#

from MCVisitor import MCVisitor
from MCParser import MCParser
from AST import *

class ASTGeneration(MCVisitor):
    def visitProgram(self,ctx:MCParser.ProgramContext):
        list_declaration = [self.visit(ctx.getChild(i)) for i in range(ctx.getChildCount()-1)]
        declarations = []
        for x in list_declaration:
            if isinstance(x, list):
                declarations += x
            else:
                declarations += [x]
        return Program(declarations)

    # ------------  Vardeclaration  ------------------
    def visitDeclaration(self, ctx:MCParser.DeclarationContext):
        return self.visit(ctx.getChild(0))

    def visitVardeclaration(self, ctx:MCParser.VardeclarationContext):
        listVardec = []
        typeVariable =  self.visit(ctx.singletype())
        list_id = self.visit(ctx.idlist())
        for x in list_id:
            if not isinstance(x, list):
                listVardec += [VarDecl(x, typeVariable)]
            else:
                listVardec += [VarDecl(x[0], ArrayType(x[1], typeVariable))]
        return listVardec

    def visitSingletype(self, ctx:MCParser.SingletypeContext):
        if ctx.INTTYPE():
            return IntType()
        elif ctx.FLOATTYPE():
            return FloatType()
        elif ctx.BOOLTYPE():
            return BoolType()
        else:
            return StringType()

    def visitIdlist(self, ctx:MCParser.IdlistContext):
        return [self.visit(x) for x in ctx.idtail()]

    def visitIdtail(self, ctx:MCParser.IdtailContext):
        return self.visit(ctx.getChild(0))

    # # idarray: ID LSB INTLIT RSB;
    def visitIdarray(self, ctx:MCParser.IdarrayContext):
        return [ctx.ID().getText(), ctx.INTLIT().getText()]

    def visitIdsingle(self, ctx:MCParser.IdsingleContext):
        return ctx.ID().getText()

    # ------------  Funcdeclaration  ------------------
    def visitFuncdeclaration(self,ctx:MCParser.FuncdeclarationContext):
        if ctx.VOIDTYPE():
            returnType = VoidType()
        else:
            returnType = self.visit(ctx.getChild(0))
        name = ctx.ID().getText()
        listParam = []
        if ctx.paralist_decla():
            params = self.visit(ctx.paralist_decla())
            for x in params:
                if len(x) == 2:
                    listParam += [VarDecl(x[1], x[0])]
                else:
                    listParam += [VarDecl(x[1], ArrayPointerType(x[0]))]

        body = self.visit(ctx.block())
        return FuncDecl(Id(name),listParam, returnType, body)

    # ---- Array Pointer Type  -----
    def visitArraypointertype(self,ctx:MCParser.ArraypointertypeContext):
        return ArrayPointerType(self.visit(ctx.singletype()))

    # ----- List Parameter Declaration -------
    def visitParalist_decla(self, ctx:MCParser.Paralist_declaContext):
        return [self.visit(x) for x in ctx.paradecla()]

    # ----- Parameter Declaration ------
    def visitParadecla(self, ctx:MCParser.ParadeclaContext):
        if ctx.getChildCount() == 2:
            return [self.visit(ctx.singletype()), self.visit(ctx.idsingle())]
        else:
            return [self.visit(ctx.singletype()), self.visit(ctx.idsingle()),'[',']']

	# ----- Block in function declaration ---------
    def visitBlock(self, ctx:MCParser.BlockContext):
        listBlock = []
        if ctx.vardeclaration():
            listBlock += [self.visit(x) for x in ctx.vardeclaration()]
        elif ctx.statement():
            listBlock += [self.visit(x) for x in ctx.statement()]

        list_element = [self.visit(ctx.getChild(i+1)) for i in range(ctx.getChildCount() - 2)]
        element = []
        for x in list_element:
            if isinstance(x, list):
                element += x
            else:
                element += [x]

        return Block(element)

    # ----- Statement -----------
    def visitStatement(self, ctx:MCParser.StatementContext):
        return self.visit(ctx.getChild(0))

    # ----- If Statenment --------
    def visitIfstmt(self, ctx:MCParser.IfstmtContext):
        exp = self.visit(ctx.expression())
        listStatement = [self.visit(x) for x in ctx.statement()]
        thenStmt = listStatement[0]
        elseStmt = None
        if len(listStatement) != 1:
            elseStmt = listStatement[1]

        return If(exp,thenStmt) if elseStmt is None else If(exp, thenStmt, elseStmt)

    # ----- Do While Statenment --------
    def visitDowhilestmt(self,ctx:MCParser.DowhilestmtContext):
        list_stmt = []
        exp = self.visit(ctx.expression())
        if ctx.statement():
            list_stmt += [self.visit(x) for x in ctx.statement()]
        return Dowhile(list_stmt, exp)

    # ----- For Statenment --------
    def visitForstmt(self,ctx:MCParser.ForstmtContext):
        list_exp = [self.visit(x) for x in ctx.expression()]
        exp1 = list_exp[0]
        exp2 = list_exp[1]
        exp3 = list_exp[2]
        loop = self.visit(ctx.statement())
        return For(exp1, exp2, exp3, loop)

    # ----- Breakstmt ------
    def visitBreak(self, ctx:MCParser.BreakstmtContext):
        return Break()

    def visitExpression(self,ctx:MCParser.ExpressionContext):
        return