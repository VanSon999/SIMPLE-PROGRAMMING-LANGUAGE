.source MPClass.java
.class public MPClass
.super java.lang.Object

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
.var 1 is ast I from Label0 to Label1
.var 2 is byz I from Label0 to Label1
.var 3 is ctx I from Label0 to Label1
Label0:
	invokestatic MPClass/too()I
	istore_3
	iload_3
	invokestatic io/putInt(I)V
Label1:
	return
.limit stack 1
.limit locals 4
.end method

.method public static too()I
.var 0 is a I from Label2 to Label3
.var 1 is b I from Label2 to Label3
Label2:
	iconst_5
	istore_0
	bipush 6
	istore_1
	iload_0
	iload_1
	if_icmple Label4
	iconst_1
	goto Label5
Label4:
	iconst_0
Label5:
	ifgt Label6
	bipush 6
	goto Label3
	goto Label7
Label6:
	iconst_5
	goto Label3
Label7:
Label3:
	ireturn
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
