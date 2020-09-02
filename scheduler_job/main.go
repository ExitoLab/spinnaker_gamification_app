package main

import (
	"fmt"
	"io/ioutil"
	"net/http"
)

func main() {
	resp, err := http.Get("curl -X GET -u ExitoLab:9d82da6de5c01a0ebacbd11752cba900a9dc4219 https://api.github.com/repos/ExitoLab/spinnaker-ms-teams-notification-plugin/issues")
	if err != nil {
		print(err)
	}

	defer resp.Body.Close()
	body, err := ioutil.ReadAll(resp.Body)
	if err != nil {
		print(err)
	}

	fmt.Print(string(body))
}
