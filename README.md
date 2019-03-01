# [shiriki]
shiriki is an online platform that enables students to share books easily and get access to marking scheme of past papers


### End points
Method | Endpoint | Usage |
| ---- | ---- | --------------- |
|POST| `/api/v1/auth/register/admin` |  Create an admin. |
|POST| `/api/v1/auth/register/user` |  Create a user. |
|POST| `/api/v1/auth/login/admin` |  login an admin. |
|POST| `/api/v1/auth/login/user` |  login a user. |
|POST| `/api/v1/buy-book` |  buy a book. |
|POST| `/api/v1/share-book` |  share a book. |
|GET| `/api/v1/get-books` | Get all books.|
|GET| `/api/v1/get-book/<book_id>` | Get one book. |
|DELETE| `/api/v1/book/<flag_id>` | remove a book. |

## License

Shitiki is released under the [MIT License](shiriki-/LICENSE).
