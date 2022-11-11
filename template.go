package template

import (
	"fmt"
	"log"
	"os"
	"reflect"
	"strings"
	"text/template"

	// "github.com/flosch/pongo2/v5"
	"gopkg.in/osteele/liquid.v1"
)

// func main() {

// 	// rd := RenderData{
// 	// 	// ObjectID:   12321,
// 	// 	// ObjectName: "aaaa",
// 	// }

// 	path := "mappings/audit_test.json"
// 	// err := Render(path, rd)
// 	// if err != nil {
// 	// 	panic(err)
// 	// }

// 	rm := map[string]interface{}{
// 		"object_id1":   321,
// 		"object_name1": "aaa",
// 		"env_flag":     1,
// 	}
// 	err := Render2(path, rm)
// 	if err != nil {
// 		panic(err)
// 	}

// }

type RenderData struct {
	ObjectID   int    `json:"object_id"`
	ObjectName string `json:"object_name"`
}

func Render(mappingFilePath string, renderData RenderData) error {

	data, err := os.ReadFile(mappingFilePath)
	if err != nil {
		return fmt.Errorf("error reading mapping file: %s, err: %w", mappingFilePath, err)
	}

	funcMap := template.FuncMap{
		// The name "title" is what the function will be called in the template text.
		"title": strings.Title,
		"default": func(arg interface{}, value interface{}) interface{} {
			defer recover()

			v := reflect.ValueOf(value)
			switch v.Kind() {
			case reflect.String, reflect.Slice, reflect.Array, reflect.Map:
				if v.Len() == 0 {
					return arg
				}
			case reflect.Bool:
				if !v.Bool() {
					return arg
				}
			default:
				return value
			}

			return value
		},
	}

	tmpl := template.New("test").Delims("<<", ">>")
	parseTmp, err := tmpl.Option().Funcs(funcMap).Parse(string(data))
	if err != nil {
		return fmt.Errorf("could not parse test data as a template: %w", err)
	}

	return parseTmp.Execute(os.Stdout, renderData)

	// var buf bytes.Buffer
	// err = parseTmp.Execute(&buf, renderData)
	// fmt.Println(err)
	// if err != nil {
	// 	return err
	// }
	// fmt.Println(buf.String())

	// f, _ := os.Create(mappingFilePath)
	// err = os.WriteFile(mappingFilePath, buf.Bytes(), 0644)
	// if err != nil {
	// 	return err
	// }

	// defer f.Close()

	// return nil
}

func Render2(mappingFilePath string, renderMap map[string]interface{}) error {

	engine := liquid.NewEngine()
	data, err := os.ReadFile(mappingFilePath)
	if err != nil {
		return fmt.Errorf("error reading mapping file: %s, err: %w", mappingFilePath, err)
	}

	// template := `<h1>{{ page.title }}</h1>`
	// bindings := map[string]interface{}{
	// 	"page": map[string]string{
	// 		"title": "Introduction",
	// 	},
	// }

	// m := make(map[string]interface{})
	// d, _ := json.Marshal(renderData)
	// json.Unmarshal(d, &m)
	// fmt.Println(m)
	fmt.Println(renderMap)

	out, err := engine.ParseAndRender(data, renderMap)
	if err != nil {
		log.Fatalln(err)
	}
	fmt.Println(string(out))

	return nil
}
