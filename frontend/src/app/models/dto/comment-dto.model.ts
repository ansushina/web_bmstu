import {User} from './user-dto.model';

export interface Comment {
  id?: number;
  text?: string;
  author?: User;
  film?: number;
  created: string;
}
