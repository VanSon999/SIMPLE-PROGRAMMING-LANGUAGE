.source MPClass.java
.class public MPClass
.super java.lang.Object
.field static a F
.field static b I

.method public static foo(IFLjava/lang/String;Z)I
.var 0 is x I from Label0 to Label1
.var 1 is y F from Label0 to Label1
.var 2 is z Ljava/lang/String; from Label0 to Label1
.var 3 is t Z from Label0 to Label1
Label0:
	iload_0
	invokestatic io/putIntLn(I)V
	fload_1
	invokestatic io/putFloatLn(F)V
	aload_2
	invokestatic io/putStringLn(Ljava/lang/String;)V
	iload_3
	invokestatic io/putBoolLn(Z)V
	iload_0
	goto Label1
Label1:
	ireturn
.limit stack 1
.limit locals 4
.end method

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label2 to Label3
.var 1 is c Ljava/lang/String; from Label2 to Label3
.var 2 is d Z from Label2 to Label3
Label2:
	ldc 12.8700
	putstatic MPClass.a F
	bipush 10
	putstatic MPClass.b I
	ldc "PPL 10"
	astore_1
	bipush 10
	bipush 10
	if_icmpne Label4
	iconst_1
	goto Label5
Label4:
	iconst_0
Label5:
	istore_2
	getstatic MPClass.b I
	getstatic MPClass.a F
	aload_1
	iload_2
	invokestatic MPClass/foo(IFLjava/lang/String;Z)I
	i2f
	putstatic MPClass.a F
Label3:
	return
.limit stack 6
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
