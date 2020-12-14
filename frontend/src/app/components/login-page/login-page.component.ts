import {Component, OnInit} from '@angular/core';
import {UserService} from "../../services/user.service";
import {ActivatedRoute, Router} from "@angular/router";

@Component({
  selector: 'app-login-page',
  templateUrl: './login-page.component.html',
  styleUrls: ['./login-page.component.scss']
})
export class LoginPageComponent implements OnInit {

  constructor(private route: ActivatedRoute, private router: Router, private userService: UserService) {
  }

  public username = '';
  public password = '';
  public error401;
  public error400;
  public error;

  onLogin(): void {
    this.userService.login(this.username, this.password).subscribe(
      session => {
        localStorage.setItem('user-token', session.token);
        localStorage.setItem('username', session.username);
        localStorage.setItem('id', session.id.toString());
        this.router.navigate(['/home']);
      },
        error => {
         if (error.status === 401) {
           this.error401 = error;
           this.error400 = null;
           this.error = null;
         } else if (error.status === 400) {
           this.error400 = error;
           this.error401 = null;
           this.error = null;
         } else {
           this.error = error;
           this.error400 =  null;
           this.error401 = null;
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
