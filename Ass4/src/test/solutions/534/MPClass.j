.source MPClass.java
.class public MPClass
.super java.lang.Object
.field static x I
.field static y I
.field static z I

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
	getstatic MPClass.x I
	iconst_0
	if_icmpne Label2
	iconst_1
	goto Label3
Label2:
	iconst_0
Label3:
	getstatic MPClass.x I
	iconst_1
	if_icmpne Label4
	iconst_1
	goto Label5
Label4:
	iconst_0
Label5:
	ior
	ifgt Label6
	iconst_2
	invokestatic io/putIntLn(I)V
	goto Label7
Label6:
	iconst_1
	invokestatic io/putIntLn(I)V
Label7:
Label1:
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
