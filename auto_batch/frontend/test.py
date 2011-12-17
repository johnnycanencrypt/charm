import ast
from ASTParser import *

class AST_Test(ast.NodeVisitor):
	def __init__(self):
		self.my = ASTParser()

	def visit_FunctionDef(self, node):
		print(type(node.args.args[0].arg).__name__)

def verify():
	pk = {4:5, 'x':'10'}
	if (1 == 1):
		pass

if __name__ == '__main__':
	test = ASTParser()
	node = test.getASTNodeFromFile("new.py")
	next = AST_Test()
	next.visit(node)
