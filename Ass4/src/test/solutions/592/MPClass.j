.source MPClass.java
.class public MPClass
.super java.lang.Object
.field static ist I

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
	bipush 90
	putstatic MPClass.ist I
Label2:
	getstatic MPClass.ist I
	iconst_0
	if_icmplt Label4
	getstatic MPClass.ist I
	bipush 10
	irem
	iconst_0
	if_icmpeq Label5
	iconst_1
	goto Label6
Label5:
	iconst_0
Label6:
	ifgt Label7
	getstatic MPClass.ist I
	i2f
	bipush 10
	i2f
	fdiv
	invokestatic io/putFloatLn(F)V
	goto Label8
Label7:
	goto Label3
Label8:
Label3:
	getstatic MPClass.ist I
	iconst_1
	isub
	putstatic MPClass.ist I
	goto Label2
Label4:
Label1:
	return
.limit stack 5
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
