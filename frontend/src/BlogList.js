import { Link } from 'react-router-dom';
import Markdown from 'markdown-to-jsx';

const BlogList = ({ blogs, title }) => {
    return (
        <div className="blog-list">
            <h2>{title}</h2>
            {blogs.map((blog) => (
                <div className="blog-preview has-white-bg" key={blog.id}>
                    <Link to={`/blogs/${blog.id}`}>
                        <div style={{ maxHeight: "320px", overflow: "hidden" }}>
                            <h2> {blog.title} </h2>
                            <p>{blog.created_at} </p>
                            <Markdown>{blog.body}</Markdown>
                        </div>
                    </Link>
                </div>
            ))}
        </div>
    );
}

export default BlogList;