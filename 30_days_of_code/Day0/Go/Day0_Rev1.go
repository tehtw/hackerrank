package main
import (
        "fmt"
        "bufio"
        "os"
)

func main() {
        input_reader := bufio.NewReader(os.Stdin)
        input, _ := input_reader.ReadString('\n')
        fmt.Print("Hello, World.\n")
        fmt.Print(input)
}
