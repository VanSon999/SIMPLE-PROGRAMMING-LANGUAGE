.source MPClass.java
.class public MPClass
.super java.lang.Object
.field static Num_f F

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
.var 1 is Num_t I from Label0 to Label1
Label0:
	bipush 12
	istore_1
	iload_1
	i2f
	putstatic MPClass.Num_f F
	getstatic MPClass.Num_f F
	invokestatic io/putFloat(F)V
Label1:
	return
.limit stack 1
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
