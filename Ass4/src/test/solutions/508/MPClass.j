.source MPClass.java
.class public MPClass
.super java.lang.Object

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
	bipush 14
	i2f
	ldc 2.0000
	fneg
	fdiv
	invokestatic io/putFloatLn(F)V
	bipush 13
	i2f
	ldc 2.0878
	fmul
	invokestatic io/putFloatLn(F)V
	ldc 158.2036
	ldc 236.2569
	fneg
	fmul
	invokestatic io/putFloatLn(F)V
	ldc 122.2376
	bipush 9
	i2f
	fmul
	invokestatic io/putFloat(F)V
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
