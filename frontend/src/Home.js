import BlogList from "./BlogList";
import useFetch from "./useFetch";


const Home = () => {
    const api = process.env.REACT_APP_API_URL;
    const { data: blogs, isPending, error } = useFetch(`${api}/api/blogs/`);

    return (
        <div className="home">
            {error && <div>{ error }</div>}
            {isPending && <div>Loading...</div>}
            {blogs && <BlogList blogs={blogs} title='All blogs!' />}
        </div>
    );
}
 
export default Home;