.source MPClass.java
.class public MPClass
.super java.lang.Object

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
	ldc 2147483648
	ineg
	invokestatic io/putIntLn(I)V
	ldc 1000000000
	ineg
	ldc 65565654
	iadd
	invokestatic io/putIntLn(I)V
	ldc 1000000000
	ineg
	i2f
	ldc 65565654
	i2f
	fdiv
	invokestatic io/putFloatLn(F)V
	ldc 2147483647
	invokestatic io/putIntLn(I)V
Label1:
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
