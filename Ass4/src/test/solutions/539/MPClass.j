.source MPClass.java
.class public MPClass
.super java.lang.Object
.field static x F

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
.var 1 is i I from Label0 to Label1
Label0:
	iconst_0
	i2f
	putstatic MPClass.x F
	iconst_1
	istore_1
	iload_1
	iconst_2
	if_icmpne Label2
	iconst_1
	goto Label3
Label2:
	iconst_0
Label3:
	ifgt Label4
	iload_1
	iconst_1
	if_icmpne Label6
	iconst_1
	goto Label7
Label6:
	iconst_0
Label7:
	ifgt Label8
	goto Label9
Label8:
	getstatic MPClass.x F
	iconst_0
	i2f
	fcmpl
	ifne Label10
	iconst_1
	goto Label11
Label10:
	iconst_0
Label11:
	ifgt Label12
	goto Label13
Label12:
	ldc 0.0000
	bipush 10
	i2f
	fcmpl
	ifne Label14
	iconst_1
	goto Label15
Label14:
	iconst_0
Label15:
	ifgt Label16
	iload_1
	i2f
	invokestatic io/putFloatLn(F)V
	goto Label17
Label16:
	ldc "No10"
	invokestatic io/putStringLn(Ljava/lang/String;)V
Label17:
Label13:
Label9:
	goto Label5
Label4:
	ldc "No10"
	invokestatic io/putStringLn(Ljava/lang/String;)V
Label5:
Label1:
	return
.limit stack 9
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
