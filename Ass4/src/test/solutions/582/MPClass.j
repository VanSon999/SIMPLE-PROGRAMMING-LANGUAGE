.source MPClass.java
.class public MPClass
.super java.lang.Object
.field static ctx I

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
.var 1 is iy I from Label0 to Label1
Label0:
	iconst_1
	istore_1
	iconst_0
	putstatic MPClass.ctx I
	getstatic MPClass.ctx I
	iconst_1
	iadd
	istore_1
Label2:
	iload_1
	iconst_3
	if_icmpgt Label4
	iload_1
	invokestatic io/putInt(I)V
Label3:
	iload_1
	iconst_1
	iadd
	istore_1
	goto Label2
Label4:
	iconst_3
	istore_1
Label5:
	iload_1
	getstatic MPClass.ctx I
	iconst_1
	iadd
	if_icmplt Label7
	iload_1
	invokestatic io/putInt(I)V
Label6:
	iload_1
	iconst_1
	isub
	istore_1
	goto Label5
Label7:
Label1:
	return
.limit stack 4
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
