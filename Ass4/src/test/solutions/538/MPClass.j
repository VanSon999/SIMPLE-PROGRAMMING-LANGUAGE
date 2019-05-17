.source MPClass.java
.class public MPClass
.super java.lang.Object
.field static x F

.method public static foo(FI)I
.var 0 is a F from Label0 to Label1
.var 1 is b I from Label0 to Label1
Label0:
	fload_0
	invokestatic io/putFloatLn(F)V
	iload_1
	bipush 12
	iadd
	goto Label1
Label1:
	ireturn
.limit stack 2
.limit locals 2
.end method

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label2 to Label3
Label2:
	bipush 12
	i2f
	iconst_4
	invokestatic MPClass/foo(FI)I
	i2f
	putstatic MPClass.x F
	getstatic MPClass.x F
	invokestatic io/putFloatLn(F)V
Label3:
	return
.limit stack 2
.limit locals 1
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
