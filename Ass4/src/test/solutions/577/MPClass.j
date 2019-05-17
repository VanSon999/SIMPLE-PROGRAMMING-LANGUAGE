.source MPClass.java
.class public MPClass
.super java.lang.Object
.field static n I

.method public static foo1(I)I
.var 0 is n I from Label0 to Label1
Label0:
	iload_0
	iconst_0
	if_icmpne Label2
	iconst_1
	goto Label3
Label2:
	iconst_0
Label3:
	ifgt Label4
	goto Label5
Label4:
	iconst_0
	goto Label1
Label5:
	iload_0
	invokestatic io/putIntLn(I)V
	iload_0
	iconst_1
	isub
	invokestatic MPClass/foo2(I)I
	goto Label1
Label1:
	ireturn
.limit stack 5
.limit locals 1
.end method

.method public static foo2(I)I
.var 0 is n I from Label6 to Label7
Label6:
	iload_0
	iconst_0
	if_icmpne Label8
	iconst_1
	goto Label9
Label8:
	iconst_0
Label9:
	ifgt Label10
	goto Label11
Label10:
	iconst_0
	goto Label7
Label11:
	iload_0
	invokestatic io/putIntLn(I)V
	iload_0
	iconst_1
	isub
	invokestatic MPClass/foo3(I)I
	goto Label7
Label7:
	ireturn
.limit stack 8
.limit locals 1
.end method

.method public static foo3(I)I
.var 0 is n I from Label12 to Label13
Label12:
	iload_0
	iconst_0
	if_icmpne Label14
	iconst_1
	goto Label15
Label14:
	iconst_0
Label15:
	ifgt Label16
	goto Label17
Label16:
	iconst_0
	goto Label13
Label17:
	iload_0
	invokestatic io/putIntLn(I)V
	iload_0
	iconst_1
	isub
	invokestatic MPClass/foo1(I)I
	goto Label13
Label13:
	ireturn
.limit stack 11
.limit locals 1
.end method

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label18 to Label19
.var 1 is x I from Label18 to Label19
Label18:
	bipush 10
	putstatic MPClass.n I
	getstatic MPClass.n I
	invokestatic MPClass/foo1(I)I
	istore_1
Label19:
	return
.limit stack 10
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
