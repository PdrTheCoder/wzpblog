import BlogList from "./BlogList";
import useFetch from "./useFetch";

const Home = () => {
    const { data: blogs, isPending, error } = useFetch('http://127.0.0.1:5000/api/blogs/');

    return (
        <div className="home">
            {error && <div>{ error }</div>}
            {isPending && <div>Loading...</div>}
            {blogs && <BlogList blogs={blogs} title='All blogs!' />}
        </div>
    );
}
 
export default Home;