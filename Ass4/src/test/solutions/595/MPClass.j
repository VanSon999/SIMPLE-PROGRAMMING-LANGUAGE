.source MPClass.java
.class public MPClass
.super java.lang.Object
.field static ast F
.field static byz F
.field static ctx F
.field static out Z

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
	iconst_1
	i2f
	putstatic MPClass.ast F
	iconst_2
	i2f
	putstatic MPClass.byz F
	iconst_4
	i2f
	putstatic MPClass.ctx F
	getstatic MPClass.ast F
	getstatic MPClass.byz F
	fdiv
	getstatic MPClass.ctx F
	fdiv
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
