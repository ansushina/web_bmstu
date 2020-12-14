import {Component, OnInit} from '@angular/core';
import {ActivatedRoute, Router} from '@angular/router';
import {UserService} from '../../services/user.service';

@Component({
  selector: 'app-registaration-page',
  templateUrl: './registaration-page.component.html',
  styleUrls: ['./registaration-page.component.scss']
})
export class RegistarationPageComponent implements OnInit {

  public username = '';
  public password = '';
  public repeatPassword = '';
  public email = '';
  public error: string;

  constructor(private route: ActivatedRoute, private router: Router, private userService: UserService) {
  }

  onRegister(): void {
    if (this.password !== this.repeatPassword) {
      this.error = 'Пароли не совпадают.';
      return;
    }
    const user = {
      username: this.username,
      email: this.email,
      password: this.password,
    };
    this.userService.createUser(user).subscribe(
      newuser => {
        this.userService.login(user.username, user.password).subscribe(
          session => {
            localStorage.setItem('user-token', session.token);
            localStorage.setItem('username', session.username);
            localStorage.setItem('id', session.id.toString());
            this.router.navigate(['/home']);
          },
          error => console.log(error)
        );
      },
      error => {
        if (error.status === 401) {
          this.error = 'Неправильные данные.';
        } else if (error.status === 400) {
          if (error.error.detail === 'invalid_email') {
            this.error = 'Пользователь с таким email уже существует.';
          } else if (error.error.detail === 'invalid_username'){
            this.error = 'Пользователь с таким именем уже существует.';
          } else {
            this.error = 'Произошла ошибка, проверьте, что все поля заполнены верно.';
          }
        } else {
          this.error = 'Ошибка на cервере';
        }
      }
    );
  }

  ngOnInit(): void {
    if (localStorage.getItem('username')) {
      this.router.navigate(['/']);
    }
  }

}
