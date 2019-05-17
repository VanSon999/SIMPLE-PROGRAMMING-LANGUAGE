.source MPClass.java
.class public MPClass
.super java.lang.Object

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
.var 1 is iat I from Label0 to Label1
.var 2 is jr I from Label0 to Label1
Label0:
	bipush 7
	istore_1
	iconst_2
	istore_2
	bipush 9
	i2f
	ldc 3.0000
	fdiv
	invokestatic io/putFloatLn(F)V
	ldc 9.0000
	ldc 3.0000
	fdiv
	invokestatic io/putFloatLn(F)V
	ldc 9.0000
	iconst_3
	i2f
	fdiv
	invokestatic io/putFloatLn(F)V
	bipush 6
	i2f
	iconst_3
	i2f
	fdiv
	ldc 1.5000
	iconst_3
	i2f
	fdiv
	fadd
	invokestatic io/putFloatLn(F)V
	iload_1
	i2f
	iload_2
	iconst_5
	iadd
	i2f
	fdiv
	invokestatic io/putFloatLn(F)V
Label1:
	return
.limit stack 3
.limit locals 3
.end method

.method public <init>()V
.var 0 is this LMPClass; from Label0 to Label1
Label0:
	aload_0
	invokespecial java/lang/Object/<init>()V
Label1:
	return
.limit stack 1
.limit locals 1
.end method
