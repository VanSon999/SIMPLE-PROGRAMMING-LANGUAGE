.source MPClass.java
.class public MPClass
.super java.lang.Object

.method public static chia()F
Label0:
	bipush 9
	i2f
	bipush 9
	i2f
	fdiv
	goto Label1
Label1:
	freturn
.limit stack 2
.limit locals 0
.end method

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label2 to Label3
Label2:
	bipush 100
	i2f
	invokestatic MPClass/chia()F
	fmul
	bipush 100
	i2f
	fmul
	ldc 10000.0000
	fsub
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
