package main
import (
	"fmt"
	"bufio"
	"os"
)

func main() {
	input_reader := bufio.NewScanner(os.Stdin)
	for input_reader.Scan() {
	fmt.Print("Hello, World.\n")
	fmt.Print(input_reader.Text())
}
}
