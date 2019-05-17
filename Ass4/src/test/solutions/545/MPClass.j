.source MPClass.java
.class public MPClass
.super java.lang.Object
.field static x F
.field static y F
.field static z F

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
.var 1 is x I from Label0 to Label1
Label0:
	bipush 20
	i2f
	putstatic MPClass.y F
	getstatic MPClass.y F
	invokestatic io/putFloatLn(F)V
Label2:
.var 2 is y F from Label2 to Label3
	bipush 10
	i2f
	fstore_2
	fload_2
	invokestatic io/putFloatLn(F)V
Label4:
.var 3 is y F from Label4 to Label5
	bipush 15
	i2f
	fstore_3
	fload_3
	invokestatic io/putFloatLn(F)V
Label5:
	fload_2
	bipush 15
	i2f
	fcmpl
	ifne Label6
	iconst_1
	goto Label7
Label6:
	iconst_0
Label7:
	ifgt Label8
	fload_2
	invokestatic io/putFloatLn(F)V
	goto Label9
Label8:
	bipush 15
	i2f
	invokestatic io/putFloatLn(F)V
Label9:
Label3:
	getstatic MPClass.y F
	invokestatic io/putFloatLn(F)V
Label1:
	return
.limit stack 3
.limit locals 4
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
