.source MPClass.java
.class public MPClass
.super java.lang.Object
.field static n I

.method public static foo(Ljava/lang/String;I)Ljava/lang/String;
.var 0 is x Ljava/lang/String; from Label0 to Label1
.var 1 is num I from Label0 to Label1
.var 2 is i I from Label0 to Label1
Label0:
	iconst_1
	istore_2
Label2:
	iload_2
	iload_1
	if_icmpgt Label4
	aload_0
	invokestatic io/putStringLn(Ljava/lang/String;)V
Label3:
	iload_2
	iconst_1
	iadd
	istore_2
	goto Label2
Label4:
	getstatic MPClass.n I
	iconst_1
	iadd
	putstatic MPClass.n I
	getstatic MPClass.n I
	bipush 20
	if_icmple Label5
	iconst_1
	goto Label6
Label5:
	iconst_0
Label6:
	ifgt Label7
	ldc "PPL"
	iconst_5
	invokestatic MPClass/foo(Ljava/lang/String;I)Ljava/lang/String;
	goto Label1
	goto Label8
Label7:
	ldc "END"
	goto Label1
Label8:
Label1:
	areturn
.limit stack 5
.limit locals 3
.end method

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label9 to Label10
Label9:
	bipush 15
	putstatic MPClass.n I
	ldc "ppl"
	iconst_5
	invokestatic MPClass/foo(Ljava/lang/String;I)Ljava/lang/String;
	invokestatic io/putString(Ljava/lang/String;)V
Label10:
	return
.limit stack 6
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
