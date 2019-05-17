.source MPClass.java
.class public MPClass
.super java.lang.Object

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
.var 1 is x I from Label0 to Label1
Label0:
	ldc "PPL \n 2018"
	invokestatic io/putString(Ljava/lang/String;)V
	invokestatic io/putLn()V
	ldc "PPL \n 2018"
	invokestatic io/putStringLn(Ljava/lang/String;)V
	iconst_1
	invokestatic io/putBool(Z)V
	iconst_0
	invokestatic io/putBoolLn(Z)V
	bipush 45
	i2f
	invokestatic io/putFloat(F)V
	ldc 45.6000
	invokestatic io/putFloat(F)V
	bipush 45
	i2f
	invokestatic io/putFloatLn(F)V
	ldc 45.2500
	invokestatic io/putFloatLn(F)V
	bipush 89
	invokestatic io/putInt(I)V
	sipush 343
	invokestatic io/putIntLn(I)V
Label1:
	return
.limit stack 3
.limit locals 2
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
