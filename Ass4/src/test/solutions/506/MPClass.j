.source MPClass.java
.class public MPClass
.super java.lang.Object

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
	iconst_1
	iconst_2
	isub
	invokestatic io/putIntLn(I)V
	iconst_1
	i2f
	ldc 2.0000
	fsub
	invokestatic io/putFloatLn(F)V
	ldc 1.2300
	ldc 9.3400
	fneg
	fsub
	invokestatic io/putFloatLn(F)V
	ldc 1.2376
	bipush 9
	ineg
	i2f
	fsub
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
