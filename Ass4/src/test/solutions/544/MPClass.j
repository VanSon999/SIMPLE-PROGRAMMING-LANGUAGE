.source MPClass.java
.class public MPClass
.super java.lang.Object
.field static x F

.method public static foo1()F
Label0:
	bipush 10
	i2f
	goto Label1
Label1:
	freturn
.limit stack 1
.limit locals 0
.end method

.method public static foo()V
Label2:
	bipush 20
	invokestatic io/putIntLn(I)V
	goto Label3
Label3:
	return
.limit stack 1
.limit locals 0
.end method

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label4 to Label5
Label4:
	invokestatic MPClass/foo()V
	invokestatic MPClass/foo1()F
	invokestatic io/putFloat(F)V
Label5:
	return
.limit stack 1
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
