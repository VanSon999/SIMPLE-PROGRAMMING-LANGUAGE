.source MPClass.java
.class public MPClass
.super java.lang.Object
.field static x F

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
	bipush 15
	i2f
	iconst_3
	i2f
	fdiv
	putstatic MPClass.x F
	getstatic MPClass.x F
	iconst_5
	i2f
	fcmpl
	ifne Label2
	iconst_1
	goto Label3
Label2:
	iconst_0
Label3:
	ifgt Label4
	goto Label5
Label4:
Label6:
.var 1 is x F from Label6 to Label7
	bipush 15
	i2f
	fstore_1
	fload_1
	bipush 15
	i2f
	fcmpl
	ifne Label8
	iconst_1
	goto Label9
Label8:
	iconst_0
Label9:
	ifgt Label10
	goto Label11
Label10:
	fload_1
	invokestatic io/putFloatLn(F)V
Label11:
Label7:
	getstatic MPClass.x F
	iconst_5
	i2f
	fcmpl
	ifne Label12
	iconst_1
	goto Label13
Label12:
	iconst_0
Label13:
	ifgt Label14
	goto Label15
Label14:
	getstatic MPClass.x F
	getstatic MPClass.x F
	fmul
	getstatic MPClass.x F
	fmul
	getstatic MPClass.x F
	fsub
	putstatic MPClass.x F
Label15:
	getstatic MPClass.x F
	invokestatic io/putFloatLn(F)V
Label5:
Label1:
	return
.limit stack 8
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
