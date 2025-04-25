@lista2 = global [3 x i32] [i32 0, i32 3, i32 -4]

define i32 @main() {
entry:
  %array_ptr = getelementptr [3 x i32], [3 x i32]* @lista2, i32 0, i32 1
  %value = load i32, i32* %array_ptr

  %ctrl_c = alloca i32
  store i32 %value, i32* %ctrl_c

  %result = load i32, i32* %ctrl_c
  ret i32 %result
}