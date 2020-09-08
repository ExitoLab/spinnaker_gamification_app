package github

import (
	"encoding/json"
	"fmt"
	"log"
	"net/http"
)

type Issue struct {
	URL                   string        `json:"url"`
	RepositoryURL         string        `json:"repository_url"`
	LabelsURL             string        `json:"labels_url"`
	CommentsURL           string        `json:"comments_url"`
	EventsURL             string        `json:"events_url"`
	HTMLURL               string        `json:"html_url"`
	ID                    int64         `json:"id"`
	NodeID                string        `json:"node_id"`
	Number                int64         `json:"number"`
	Title                 string        `json:"title"`
	User                  User          `json:"user"`
	Labels                []interface{} `json:"labels"`
	State                 string        `json:"state"`
	Locked                bool          `json:"locked"`
	Assignee              interface{}   `json:"assignee"`
	Assignees             []interface{} `json:"assignees"`
	Milestone             interface{}   `json:"milestone"`
	Comments              int64         `json:"comments"`
	CreatedAt             string        `json:"created_at"`
	UpdatedAt             string        `json:"updated_at"`
	ClosedAt              interface{}   `json:"closed_at"`
	AuthorAssociation     string        `json:"author_association"`
	ActiveLockReason      interface{}   `json:"active_lock_reason"`
	PullRequest           PullRequest   `json:"pull_request"`
	Body                  string        `json:"body"`
	PerformedViaGithubApp interface{}   `json:"performed_via_github_app"`
}

type PullRequest struct {
	URL      string `json:"url"`
	HTMLURL  string `json:"html_url"`
	DiffURL  string `json:"diff_url"`
	PatchURL string `json:"patch_url"`
}

type User struct {
	Login             string `json:"login"`
	ID                int64  `json:"id"`
	NodeID            string `json:"node_id"`
	AvatarURL         string `json:"avatar_url"`
	GravatarID        string `json:"gravatar_id"`
	URL               string `json:"url"`
	HTMLURL           string `json:"html_url"`
	FollowersURL      string `json:"followers_url"`
	FollowingURL      string `json:"following_url"`
	GistsURL          string `json:"gists_url"`
	StarredURL        string `json:"starred_url"`
	SubscriptionsURL  string `json:"subscriptions_url"`
	OrganizationsURL  string `json:"organizations_url"`
	ReposURL          string `json:"repos_url"`
	EventsURL         string `json:"events_url"`
	ReceivedEventsURL string `json:"received_events_url"`
	Type              string `json:"type"`
	SiteAdmin         bool   `json:"site_admin"`
}

func GetIssue(org string, repo string) []Issue {
	uri := fmt.Sprintf("https://api.github.com/repos/%s/%s/issues", org, repo)
	req, err := http.NewRequest("GET", uri, nil)
	if err != nil {
		log.Fatalln(err)
	}
	token := ""
	req.Header.Set("Authorization", "Bearer "+token)
	client := &http.Client{}
	res, err := client.Do(req)

	if err != nil {
		log.Fatalln(err)
	}

	defer res.Body.Close()

	var issue []Issue
	err = json.NewDecoder(res.Body).Decode(&issue)
	if err != nil {
		log.Fatalln(err)
	}

	for _, element := range issue {
		//fmt.Println("At index", index, "value is", element.User.login)
		fmt.Println(element.User.Login, element.Number, element.URL, element.CreatedAt, element.UpdatedAt)
	}

	return Issue

	//fmt.Printf("Issue\n\t number: %d\n\tissuetitle: %s", issue[0].Number, issue[0].Title)
	//
}
