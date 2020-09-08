package main

import (
	"log"
	"net/http"

	_ "github.com/lib/pq"

	"github.com/ExitoLab/spinnaker_gamification_app/scheduler_job/controllers"
	"github.com/gorilla/mux"
)

// func main() {
// 	fetchIssue("ExitoLab", "spinnaker-ms-teams-notification-plugin")

// 	databaseConnection()
// }

func main() {
	router := mux.NewRouter()

	router.HandleFunc("/get_issues", controllers.GetIssue).Methods("GET")

	// Swagger
	router.PathPrefix("/swagger").Handler(httpSwagger.WrapHandler)
	log.Fatal(http.ListenAndServe(":8080", router))
}

// func fetchIssue(org string, repo string) {
// 	uri := fmt.Sprintf("https://api.github.com/repos/%s/%s/issues", org, repo)
// 	req, err := http.NewRequest("GET", uri, nil)
// 	if err != nil {
// 		log.Fatalln(err)
// 	}
// 	token := ""
// 	req.Header.Set("Authorization", "Bearer "+token)
// 	client := &http.Client{}
// 	res, err := client.Do(req)

// 	if err != nil {
// 		log.Fatalln(err)
// 	}

// 	defer res.Body.Close()

// 	var issue []Issue
// 	err = json.NewDecoder(res.Body).Decode(&issue)
// 	if err != nil {
// 		log.Fatalln(err)
// 	}

// 	for _, element := range issue {
// 		//fmt.Println("At index", index, "value is", element.User.login)
// 		fmt.Println(element.User.Login, element.Number, element.URL, element.CreatedAt, element.UpdatedAt)
// 	}

// 	//fmt.Printf("Issue\n\t number: %d\n\tissuetitle: %s", issue[0].Number, issue[0].Title)
// 	//
// }

// func databaseConnection(user string, number int, url string, createdat string, updatedat string) {

// 	const (
// 		host     = "localhost"
// 		port     = 5432
// 		user     = "postgres"
// 		password = "1234"
// 		dbname   = "spinnaker"
// 	)

// 	// connection string
// 	psqlconn := fmt.Sprintf("host=%s port=%d user=%s password=%s dbname=%s sslmode=disable", host, port, user, password, dbname)

// 	// open database
// 	db, err := sql.Open("postgres", psqlconn)

// 	if err != nil {
// 		panic(err)
// 	}

// 	// close database
// 	defer db.Close()

// 	insertDynStmt := `insert into "Students"("Name", "Roll") values($1, $2)`
// 	_, e = db.Exec(insertDynStmt, "Jane", 2)

// 	if err != nil {
// 		panic(err)
// 	}

// }
