.source MPClass.java
.class public MPClass
.super java.lang.Object

.method public static main1()V
Label0:
	iconst_1
	ifgt Label2
	goto Label1
	goto Label3
Label2:
	goto Label1
Label3:
Label1:
	return
.limit stack 2
.limit locals 0
.end method

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label4 to Label5
Label4:
	invokestatic MPClass/main1()V
	iconst_1
	ifgt Label6
	goto Label5
	goto Label7
Label6:
	goto Label5
Label7:
Label5:
	return
.limit stack 3
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
