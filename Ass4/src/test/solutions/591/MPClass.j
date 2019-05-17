.source MPClass.java
.class public MPClass
.super java.lang.Object
.field static irt I

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
	iconst_0
	putstatic MPClass.irt I
Label2:
	getstatic MPClass.irt I
	bipush 10
	if_icmpgt Label4
	getstatic MPClass.irt I
	iconst_5
	if_icmple Label5
	iconst_1
	goto Label6
Label5:
	iconst_0
Label6:
	ifgt Label7
	goto Label8
Label7:
	goto Label4
Label8:
Label3:
	getstatic MPClass.irt I
	iconst_1
	iadd
	putstatic MPClass.irt I
	goto Label2
Label4:
	getstatic MPClass.irt I
	invokestatic io/putIntLn(I)V
	iconst_0
	putstatic MPClass.irt I
Label9:
	getstatic MPClass.irt I
	bipush 100
	if_icmpgt Label11
	getstatic MPClass.irt I
	bipush 10
	if_icmplt Label12
	iconst_1
	goto Label13
Label12:
	iconst_0
Label13:
	ifgt Label14
	getstatic MPClass.irt I
	invokestatic io/putInt(I)V
	goto Label15
Label14:
	goto Label10
Label15:
Label10:
	getstatic MPClass.irt I
	iconst_1
	iadd
	putstatic MPClass.irt I
	goto Label9
Label11:
Label1:
	return
.limit stack 8
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
