import { useParams, useHistory } from "react-router-dom";
import useFetch from "./useFetch";
import Markdown from 'markdown-to-jsx';

const BlogDetails = () => {
    const { id } = useParams();
    const { data: blog, isPending, error} = useFetch('http://127.0.0.1:5000/api/blogs/' + id);
    const history = useHistory();

    const token = localStorage.getItem("token");


    const handleClick = () => {
        fetch('http://127.0.0.1:5000/api/blogs/' + id, {
            method: 'DELETE'
        }).then(() => {
            history.push('/');
        })
    }

    return (
        <div className="blog-details">
            { isPending && <div>Loading...</div> }
            { error && <div>{ error }</div> }
            { blog && (
                <article>
                    <h2>{ blog.title }</h2>
                    <Markdown>{ blog.body }</Markdown>
                </article>
                // {token && <button onClick={handleClick}>Delete</button>}
            ) }
            { token && <button onClick={handleClick}>Delete</button> }
        </div>
    );
}
 
export default BlogDetails;