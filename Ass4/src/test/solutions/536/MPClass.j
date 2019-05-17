.source MPClass.java
.class public MPClass
.super java.lang.Object
.field static x F

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
.var 1 is a I from Label0 to Label1
Label0:
	iconst_2
	ineg
	istore_1
	iload_1
	iload_1
	imul
	i2f
	putstatic MPClass.x F
	getstatic MPClass.x F
	iload_1
	i2f
	fcmpl
	iflt Label2
	iconst_1
	goto Label3
Label2:
	iconst_0
Label3:
	ifgt Label4
	goto Label5
Label4:
	getstatic MPClass.x F
	iconst_0
	i2f
	fcmpl
	ifge Label6
	iconst_1
	goto Label7
Label6:
	iconst_0
Label7:
	ifgt Label8
	iload_1
	iload_1
	imul
	istore_1
	goto Label9
Label8:
	getstatic MPClass.x F
	getstatic MPClass.x F
	fmul
	putstatic MPClass.x F
Label9:
Label5:
	iload_1
	invokestatic io/putIntLn(I)V
	getstatic MPClass.x F
	invokestatic io/putFloatLn(F)V
Label1:
	return
.limit stack 6
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
