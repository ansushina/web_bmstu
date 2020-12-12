import {Component, OnInit} from '@angular/core';
import {ActivatedRoute, Router} from "@angular/router";
import {UserService} from "../../services/user.service";

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


  constructor(private route: ActivatedRoute, private router: Router, private userService: UserService) {
  }

  onRegister(): void {
    if (this.password !== this.repeatPassword) {
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
          error => console.log(error),
        );
      },
      error => console.log(error),
    );
  }

  ngOnInit(): void {
  }

}
