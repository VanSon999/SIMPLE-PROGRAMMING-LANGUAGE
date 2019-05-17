.source MPClass.java
.class public MPClass
.super java.lang.Object

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
	bipush 7
	bipush 7
	if_icmpne Label4
	iconst_1
	goto Label5
Label4:
	iconst_0
Label5:
	iconst_0
	ior
	ifgt Label6
	bipush 7
	bipush 7
	if_icmpne Label4
	iconst_1
	goto Label5
Label4:
	iconst_0
Label5:
	iconst_0
	ior
	ifgt Label6
	iconst_0
	goto Label7
Label6:
	iconst_1
Label7:
	invokestatic io/putBoolLn(Z)V
	iconst_1
	ineg
	iconst_0
	if_icmple Label10
	iconst_1
	goto Label11
Label10:
	iconst_0
Label11:
	iconst_0
	ior
	ifgt Label12
	iconst_1
	ineg
	iconst_0
	if_icmple Label10
	iconst_1
	goto Label11
Label10:
	iconst_0
Label11:
	iconst_0
	ior
	ifgt Label12
	iconst_0
	goto Label13
Label12:
	iconst_1
Label13:
	invokestatic io/putBoolLn(Z)V
	iconst_2
	iconst_2
	if_icmplt Label16
	iconst_1
	goto Label17
Label16:
	iconst_0
Label17:
	iconst_0
	ior
	ifgt Label18
	iconst_2
	iconst_2
	if_icmplt Label16
	iconst_1
	goto Label17
Label16:
	iconst_0
Label17:
	iconst_0
	ior
	ifgt Label18
	iconst_0
	goto Label19
Label18:
	iconst_1
Label19:
	invokestatic io/putBoolLn(Z)V
	iconst_2
	iconst_2
	if_icmpge Label22
	iconst_1
	goto Label23
Label22:
	iconst_0
Label23:
	iconst_0
	ior
	ifgt Label24
	iconst_2
	iconst_2
	if_icmpge Label22
	iconst_1
	goto Label23
Label22:
	iconst_0
Label23:
	iconst_0
	ior
	ifgt Label24
	iconst_0
	goto Label25
Label24:
	iconst_1
Label25:
	invokestatic io/putBool(Z)V
Label1:
	return
.limit stack 23
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
